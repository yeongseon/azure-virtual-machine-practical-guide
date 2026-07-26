targetScope = 'resourceGroup'

@description('Azure region for all lab resources.')
param location string = resourceGroup().location

@description('Resource prefix used for lab resources.')
param resourcePrefix string = 'vmconlab'

@description('Virtual machine name.')
param vmName string = '${resourcePrefix}-vm'

@description('Network interface name.')
param nicName string = '${resourcePrefix}-nic'

@description('Virtual network name.')
param vnetName string = '${resourcePrefix}-vnet'

@description('Subnet name.')
param subnetName string = 'default'

@description('Public IP address resource name.')
param publicIpName string = '${resourcePrefix}-pip'

@description('Network security group name.')
param nsgName string = '${resourcePrefix}-nsg'

@description('Virtual machine size.')
param vmSize string = 'Standard_B1s'

@description('Linux administrator username.')
param adminUsername string = 'azureuser'

@secure()
@description('Linux administrator password. Use a temporary lab-only secret when deploying.')
param adminPassword string = '<temporary-lab-password>'

@description('Marketplace image publisher.')
param imagePublisher string = 'Canonical'

@description('Marketplace image offer.')
param imageOffer string = '0001-com-ubuntu-server-jammy'

@description('Marketplace image SKU.')
param imageSku string = '22_04-lts-gen2'

@description('Marketplace image version.')
param imageVersion string = 'latest'

@description('CIDR range allowed to reach the management port after the intentional deny rule is removed.')
param managementSourcePrefix string = '198.51.100.10/32'

@description('When true, apply an explicit high-priority deny on the management port so the admin path fails deterministically.')
param blockAdminPort bool = true

var addressSpace = '10.43.0.0/16'
var subnetPrefix = '10.43.0.0/24'
var managementPort = '22'

resource publicIp 'Microsoft.Network/publicIPAddresses@2024-05-01' = {
  name: publicIpName
  location: location
  sku: {
    name: 'Standard'
  }
  properties: {
    publicIPAllocationMethod: 'Static'
  }
}

resource nsg 'Microsoft.Network/networkSecurityGroups@2024-05-01' = {
  name: nsgName
  location: location
  properties: {
    securityRules: concat(
      [
        {
          name: 'allow-ssh-from-operator'
          properties: {
            priority: 1000
            access: 'Allow'
            direction: 'Inbound'
            protocol: 'Tcp'
            sourceAddressPrefix: managementSourcePrefix
            sourcePortRange: '*'
            destinationAddressPrefix: '*'
            destinationPortRange: managementPort
          }
        }
      ],
      blockAdminPort
        ? [
            {
              name: 'deny-ssh'
              properties: {
                priority: 900
                access: 'Deny'
                direction: 'Inbound'
                protocol: 'Tcp'
                sourceAddressPrefix: '*'
                sourcePortRange: '*'
                destinationAddressPrefix: '*'
                destinationPortRange: managementPort
              }
            }
          ]
        : []
    )
  }
}

resource vnet 'Microsoft.Network/virtualNetworks@2024-05-01' = {
  name: vnetName
  location: location
  properties: {
    addressSpace: {
      addressPrefixes: [
        addressSpace
      ]
    }
    subnets: [
      {
        name: subnetName
        properties: {
          addressPrefix: subnetPrefix
          networkSecurityGroup: {
            id: nsg.id
          }
        }
      }
    ]
  }
}

resource nic 'Microsoft.Network/networkInterfaces@2024-05-01' = {
  name: nicName
  location: location
  properties: {
    ipConfigurations: [
      {
        name: 'ipconfig1'
        properties: {
          privateIPAllocationMethod: 'Dynamic'
          publicIPAddress: {
            id: publicIp.id
          }
          subnet: {
            id: resourceId('Microsoft.Network/virtualNetworks/subnets', vnet.name, subnetName)
          }
        }
      }
    ]
  }
}

resource vm 'Microsoft.Compute/virtualMachines@2024-07-01' = {
  name: vmName
  location: location
  properties: {
    hardwareProfile: {
      vmSize: vmSize
    }
    osProfile: {
      computerName: vmName
      adminUsername: adminUsername
      adminPassword: adminPassword
      linuxConfiguration: {
        disablePasswordAuthentication: false
        provisionVMAgent: true
      }
    }
    storageProfile: {
      imageReference: {
        publisher: imagePublisher
        offer: imageOffer
        sku: imageSku
        version: imageVersion
      }
      osDisk: {
        createOption: 'FromImage'
        managedDisk: {
          storageAccountType: 'StandardSSD_LRS'
        }
      }
    }
    networkProfile: {
      networkInterfaces: [
        {
          id: nic.id
          properties: {
            primary: true
          }
        }
      ]
    }
  }
}

output vmResourceId string = vm.id
output publicIpAddress string = publicIp.properties.ipAddress
output nicResourceId string = nic.id
output effectiveBlockExpected bool = blockAdminPort
