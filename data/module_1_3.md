## Cloud Concepts: Describe cloud service types

### Infrastructure as a service (IaaS)
- Customer has maximum control of cloud resources.
- Customer has largest share of responsibility in the shared responsibility model.
- Only the physical resources are controlled by cloud provider: Physical hosts, network and data center security.
- Customer is responsible for installation and configuration, patching and updates, and security.
- **Scenarios to use IaaS**:
    - Lift-and-shift migration: Moving from on-premise to cloud with similar resources.
    - Testing and development: You have established configurations for development and test environments that you need to rapidly replicate. You can start up or shut down the different environments rapidly with an IaaS structure, while maintaining complete control.

### Platform as a service (PaaS)
- Cloud provider maintains physical resources as per IaaS.
- Cloud provider also maintain the OS, middleware, DB, development tools, and business intelligence services that make up a cloud solution. In a PaaS scenario, you don't have to worry about the licensing or patching for operating systems and databases.
- Think of PaaS like using a domain joined machine: IT maintains the device with regular updates, patches, and refreshes.
- Depending on the configuration, you or the cloud provider may be responsible for networking settings and connectivity within your cloud environment, network and application security, and the directory infrastructure.
- **Scenarios to use PaaS**:
    - Development framework: PaaS provides a framework that developers can build upon to develop or customize cloud-based applications. 
    - Analytics or business intelligence: Tools provided as a service with PaaS allow organizations to analyze and mine their data, finding insights and patterns and predicting outcomes to improve forecasting, product design decisions, investment returns, and other business decisions.

### Software as a service (SaaS)
- Most complete cloud service model from a product perspective.
- Examples: Email, financial software, messaging applications, and connectivity software. 
- Customer is responsible for the data that you put into the system, the devices that you allow to connect to the system, and the users that have access.
- Nearly everything else falls to the cloud provider.
- **Scenarios to use SaaS**:
    - Email and messaging.
    - Business productivity applications.
    - Finance and expense tracking.

![shared responsibilities of IaaS, PaaS, SaaS](https://raw.githubusercontent.com/viviensiu/Azure/main/images/shared-responsibility.svg) 

### Summary
In this module, you learned about the cloud service types and some common scenarios for each type. You also reinforced how the shared responsibility model determines your responsibilities with different cloud service types.