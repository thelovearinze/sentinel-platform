provider "aws" {
  region = "eu-west-1"
}

resource "aws_vpc" "dev_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true

  tags = {
    Name        = "Sentinel-CRM-vpc"
    ManagedBy   = "Platform-Portal"
    Owner       = "Owner"
    Environment = "Development"
  }
}

output "vpc_id" {
  value = aws_vpc.dev_vpc.id
}