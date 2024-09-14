## Cloud Concepts: Describe Cloud Computing

### What is cloud computing?
- Delivery of computing services over the internet, such as common IT infrastructure plus IoT, ML and AI.
- Services are hosted in data centers owned by cloud providers.
- You only pay for only the service you used.
- Upkeep is managed by cloud providers, e.g. backup, OS updates, 24/7 SLA
- Services typically vary by cloud providers, however, all providers would provide these 2 services:
    - Compute power: how much processing your computer can do.
    - Storage.

### Shared responsibility model
* In traditional data centers, companies are responsible for: 
    - Maintaining the physical space, security, maintaining or replacing the servers. 
    - Infrastructure and software needed to keep the datacenter up and running. 
    - Keeping all systems patched and on the correct version.
* Shared responsibility model divides these between cloud provider and consumer:
    - Cloud provider: Physical security, power, cooling, and network connectivity
    - Consumer: Data and information stored in the cloud, and access security.
* In some situations, the shared responsibility model may difer, example:
    - Cloud SQL database: Cloud provider maintains the actual database, while consumer is responsible for the data that gets ingested into the database.
    - If you deployed a virtual machine and installed an SQL database on it, you’d be responsible for database patches and updates, as well as maintaining the data and information stored in the database.
* The shared responsibility model is heavily tied into the cloud service types: 
    - IaaS: Infrastructure as a service, 
    - PaaS: Platform as a service, 
    - SaaS: Software as a service.
![shared responsibilities of IaaS, PaaS, SaaS](https://raw.githubusercontent.com/viviensiu/Azure/main/images/shared-responsibility.svg) 
* **Summary**: When using a cloud provider, you’ll always be responsible for:
    - The information and data stored in the cloud
    - Devices that are allowed to connect to your cloud (cell phones, computers, and so on)
    - The accounts and identities of the people, services, and devices within your organization

* The cloud provider is always responsible for:
    - The physical datacenter
    - The physical network
    - The physical hosts
* Your service model will determine responsibility for things like:
    - Operating systems (IaaS: customer, PaaS and SaaS: Microsoft)
    - Network controls (IaaS: customer, PaaS: shared, SaaS: Microsoft)
    - Applications (IaaS: customer, PaaS: shared, SaaS: Microsoft)
    - Identity and infrastructure (IaaS: customer, PaaS and SaaS: shared)

### Cloud models
* 3 types: Private, Public, Hybrid.
* **Private Cloud**:
    - Used by a single entity
    - Pros: Greater control
    - Cons: Greater cost, fewer benefits compared to a public cloud.
    - Could be hosted from on site datacenter, dedicated datacenter offsite, or even by a third party that has dedicated that datacenter to your company.
* **Public Cloud**:
    - Built, controlled, and maintained by a third-party cloud provider.
    - Anyone that wants to purchase cloud services can access and use resources.
* **Hybrid Cloud**:
    - Uses both public and private clouds in an inter-connected environment. 
    - Can be used to allow a private cloud to surge for temporary demand by deploying public cloud resources. 
    - Can be used to provide an extra layer of security. For example, users can flexibly choose which services to keep in public cloud and which to deploy to their private cloud infrastructure.
* Key comparative aspects between the cloud models:
    * **Public cloud**: No capital expenditures to scale up. Applications can be quickly provisioned and deprovisioned. Organizations pay only for what they use. Organizations don’t have complete control over resources and security.
    * **Private cloud**: Organizations have complete control over resources and security. Data is not collocated with other organizations’ data. Hardware must be purchased for startup and maintenance. Organizations are responsible for hardware maintenance and updates.
    * **Hybrid cloud**: Provides the most flexibility. Organizations determine where to run their applications. Organizations control security, compliance, or legal requirement.
* **Multi-cloud**: multiple cloud providers
* **Azure Arc**: Manages private/public/hybrid/multi-cloud environments.
* **Azure VMware Solution**: allows redeploy, extend and run VMWare workloads that was established in private cloud when the private cloud is migrated to in public cloud (Azure).

### Consumption-based model
* 2 types of model:
    * **Capital expenditure (CapEx)**: One-time, up-front expenditure to purchase or secure tangible resources, e.g. new building.
    * **Operational expenditure (OpEx)**: Spending money on services or products over time.
* Cloud computing falls under OpEx because cloud computing operates on a consumption-based model, it does not incur cost on physical infrastructure or its related upkeep, but you pay for the IT resources you use. This brings benefits such as:
    - No upfront costs.
    - No need to purchase and manage costly infrastructure that users might not use to its fullest potential.
    - The ability to pay for more resources when they're needed.
    - The ability to stop paying for resources that are no longer needed.
* **Cloud pricing models** uses **Pay-as-you-go pricing model**: Typically pay only for the cloud services you use, which helps you:
    - Plan and manage your operating costs.
    - Run your infrastructure more efficiently.
    - Scale as your business needs change.
Imagine that you're just renting someone else's infrastructure and return it once you don't need it anymore to cut rental costs :)

### Summary
In this module, you learned about general cloud concepts. You started with things like just understanding what cloud computing is. You also learned about the shared responsibility model and how you and your cloud provider share the responsibility of keeping your information in the cloud secure. You briefly covered the differences between the cloud models (public, private, hybrid, and multi-cloud). Then, you wrapped up with a unit on how the cloud shifts IT spend from a capital expense to an operational expense.