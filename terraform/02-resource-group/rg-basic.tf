resource "azurerm_resource_group" "xorg-dev" {
  name = "xorg-dev"
  location = "East US"
}

resource "azurerm_resource_group" "xorg-stage" {
  name = "xorg-stage"
  location = "East US"
}


resource "azurerm_resource_group" "xorg-prod" {
  name = "xorg-prod"
  location = "East US"
}