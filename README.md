## Meta Labeling

**Models taken into consideration:**
------------------------------------

* Moving Average Crossover Stragegy: When the short term moving average crosses above the long term moving average, that indicates a positive trend, and hence a buy. If it crosses from the top down, it is a short signal.

* Minervini Trend Filter

* Hedgefundie's Ultimate Adventure

* Antonacci Dual Momentum

* Radge ADX Day Trade

* Radge BBO

* Radge Weekend Trend Trader

* Bensdorp books

* Connors' 7 day high/low

**Figure 1. Meta Labeling Architecture See third reference for additional details.**

![image](https://user-images.githubusercontent.com/13305262/230697422-bf530fdd-dacf-455a-a63c-d8fa573abede.png)


```{python}
AWSTemplateFormatVersion: '2010-09-09'
Description: Trading Strategy Infrastructure

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: true
      EnableDnsHostnames: true
      InstanceTenancy: default
      Tags:
        - Key: Name
          Value: TradingStrategyVPC

  InternetGateway:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags:
        - Key: Name
          Value: TradingStrategyIGW

  VPCGatewayAttachment:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref VPC
      InternetGatewayId: !Ref InternetGateway

  PublicSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      AvailabilityZone: !Select [ 0, !GetAZs '' ]
      CidrBlock: 10.0.0.0/24
      VpcId: !Ref VPC
      MapPublicIpOnLaunch: true
      Tags:
        - Key: Name
          Value: TradingStrategyPublicSubnet

  PublicRouteTable:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC
      Tags:
      - Key: Name
        Value: TradingStrategyPublicRouteTable

```

**References**

1. Marcos Lopez de Prado. Advances in Financial Machine Learning. Lopez de Prado, M. (2018). Advances in Financial Machine Learning. United Kingdom: Wiley.
