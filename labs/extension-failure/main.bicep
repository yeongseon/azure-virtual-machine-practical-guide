targetScope = 'resourceGroup'

@description('Azure region for all lab resources.')
param location string = resourceGroup().location

@description('Resource prefix used for lab resources.')
param resourcePrefix string = 'vmextlab'

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
param adminPassword string

@description('Marketplace image publisher.')
param imagePublisher string = 'Canonical'

@description('Marketplace image offer.')
param imageOffer string = '0001-com-ubuntu-server-jammy'

@description('Marketplace image SKU.')
param imageSku string = '22_04-lts-gen2'

@description('Marketplace image version.')
param imageVersion string = 'latest'

@description('VM extension name.')
param extensionName string = 'failingCustomScript'

@description('Inline shell command that intentionally returns a non-zero exit code so the Custom Script extension fails deterministically.')
param extensionCommandToExecute string = 'bash -c "echo intentional-extension-failure > /tmp/extension-failure-marker.txt; exit 42"'

var addressSpace = '10.42.0.0/16'
var subnetPrefix = '10.42.0.0/24'

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
    securityRules: [
      {
        name: 'allow-ssh'
        properties: {
          priority: 1000
          access: 'Allow'
          direction: 'Inbound'
          protocol: 'Tcp'
          sourceAddressPrefix: '*'
          sourcePortRange: '*'
          destinationAddressPrefix: '*'
          destinationPortRange: '22'
        }
      }
    ]
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

resource failingExtension 'Microsoft.Compute/virtualMachines/extensions@2024-07-01' = {
  name: extensionName
  parent: vm
  location: location
  properties: {
    publisher: 'Microsoft.Azure.Extensions'
    type: 'CustomScript'
    typeHandlerVersion: '2.1'
    autoUpgradeMinorVersion: true
    settings: {
      commandToExecute: extensionCommandToExecute
    }
  }
}

output vmResourceId string = vm.id
output extensionResourceId string = failingExtension.id
