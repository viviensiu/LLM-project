## Microsoft Azure Fundamentals: Describe Azure architecture and services

### What is Microsoft Azure?
- Microsoft's cloud computing platform with an ever-expanding set of cloud services to help build business solutions.

- **What does Azure offer?**
    - **Bring ideas to life**: Build intelligent apps and solutions
    - **Seamlessly unify**: manage all infrastructure, data, analytics, and AI solutions on an integrated platform.
    - **Innovate on trust**: deliver innovations efficiently and securely on a trusted cloud.

### Get started with Azure Accounts
![alt text](https://github.com/viviensiu/Azure/blob/main/images/account-scope-levels.png)
* The additional resources/subscriptions help billing management.
* Multiple subscriptions can be organised into invoice sections, where each section is a line item on the invoice that shows incurred charges for that month.
* You can also setup multiple invoices on the same billing account using billing profiles, where each profile has its own invoice and payment method.

- The **Azure free account** includes:
    - Free access to popular Azure products for 12 months.
    - A credit to use for the first 30 days.
    - Access to more than 25 products that are always free.

- The **Azure free student account** includes: 
    - Free access to certain Azure services for 12 months.
    - A credit to use in the first 12 months.
    - Free access to certain software developer tools.

- Plus: 24x7 documentation, support and new services demo videos.

- The **Microsoft Learn sandbox** is a temporary subscription allows you to create Azure resources during a Learn module. Learn automatically cleans up the temporary resources for you after you've completed the module.

### Azure physical infrastructure
- 2 groups:
    - **Physical Infrastructure**: Datacenters which are grouped into Azure Regions or Azure Availability Zones
    - **Management Infrastructure**.

### Azure Regions
- Geographical area with at least one or multiple datacenters that are nearby and networked together with a low-latency network. 
- Some services or virtual machine (VM) features are only available in certain regions, such as specific VM sizes or storage types. 
- There are also some global Azure services that don't require you to select a particular region, such as Microsoft Entra ID, Azure Traffic Manager, and Azure DNS.

### Azure Availability Zones
- These are physically separate datacenters within an Azure region, minimum 3 such zones in a region. Each availability zone is: 
    * Made up of one or more datacenters equipped with independent power, cooling, and networking.
    * Set up to be an isolation boundary.
    * Connected through high-speed, private fiber-optic networks.
    * **Note**: Not all Azure Regions currently support availability zones.

![alt text](https://github.com/viviensiu/Azure/blob/main/images/availability-zones.png)
- Used to run mission-critical applications and build high-availability into your application architecture by co-locating your compute, storage, networking, and data resources within an availability zone and replicating in other availability zones. 
- Keep in mind that there could be a cost to duplicating your services and transferring data between availability zones.
- Primarily for VMs, managed disks, load balancers, and SQL databases. 
- Azure services that support availability zones fall into 3 categories:
    * **Zonal services**: You pin the resource to a specific zone (for example, VMs, managed disks, IP addresses).
    * **Zone-redundant services**: The platform replicates automatically across zones (for example, zone-redundant storage, SQL Database).
    * **Non-regional services**: Services are always available from Azure geographies and are resilient to zone-wide outages as well as region-wide outages.
-  It’s possible that an event could be so large that it impacts multiple availability zones in a single region. To provide even further resilience, Azure has Region Pairs.

### Region pairs
- Most Azure regions are paired with another region within the same geography at least 300 miles away. This helps to reduce the likelihood of events that impact an entire region.
- Not all Azure services automatically replicate data or automatically fall back from a failed region to cross-replicate to another enabled region. In these scenarios, recovery and replication must be configured by the customer.
![alt text](https://github.com/viviensiu/Azure/blob/main/images/region-pairs.png)
- Advantages of region pairs:
    * If an extensive Azure outage occurs, one region out of every pair is prioritized to make sure at least one is restored as quickly as possible for applications hosted in that region pair.
    * Planned Azure updates are rolled out to paired regions one region at a time to minimize downtime and risk of application outage.
    * Data continues to reside within the same geography as its pair (except for Brazil South) for tax- and law-enforcement jurisdiction purposes.
- Most regions are paired in two-directions (they backup each other).
- However, some regions, such as West India and Brazil South, are paired in only one direction. In a one-direction pairing, the Primary region does not provide backup for its secondary region. So, even though West India’s secondary region is South India, South India does not rely on West India. West India's secondary region is South India, but South India's secondary region is Central India. Brazil South is unique because it's paired with a region outside of its geography. Brazil South's secondary region is South Central US. The secondary region of South Central US isn't Brazil South.

### Sovereign Regions
- Instances of Azure that are isolated from the main instance of Azure. For compliance or legal purposes.
- Examples:
    * US DoD Central, US Gov Virginia, US Gov Iowa and more: These regions are physical and logical network-isolated instances of Azure for U.S. government agencies and partners. These datacenters are operated by screened U.S. personnel and include additional compliance certifications.
    * China East, China North, and more: These regions are available through a unique partnership between Microsoft and 21Vianet, whereby Microsoft doesn't directly maintain the datacenters.

### Azure Management Infrastructure
- Includes Azure resources and resource groups, subscriptions, and accounts.

### Azure resources and resource groups
- Resource: Basic building block of Azure. 
- Resource groups: A group of resources. Each resource must be associated with one resource group and one group only, they can be moved to different resource groups but the former group(s) are no longer associated once moved.
- Resource groups cannot be nested.
- An action to a resource group affects all resources in the group. Hence this is something important to take note of when provisioning resources.
![alt text](https://github.com/viviensiu/Azure/blob/main/images/resource-group.png)

### Azure subscriptions
- A unit of management, billing, and scale.
- Subscriptions allow you to logically organize your resource groups and facilitate billing.
![alt text](https://github.com/viviensiu/Azure/blob/main/images/subscriptions.png)
- Using Azure requires min. one subscription. A subscription provides you with authenticated and authorized access to Azure products and services. It also allows you to provision resources. 
- An Azure subscription links to an Azure account, which is an identity in Microsoft Entra ID or in a directory that Microsoft Entra ID trusts.  
- In a multi-subscription account, you can use the subscriptions to:        
    * Configure different billing models. 
    * Apply different access-management policies. 
    * Define boundaries around Azure products, services, and resources.
- 2 types of subscription boundaries:
    * **Billing boundary**: This subscription type determines how an Azure account is billed for using Azure. Azure generates separate billing reports and invoices for each subscription so that you can organize and manage costs.
    * **Access control boundary**: Azure applies access-management policies at the subscription level, and you can create separate subscriptions to reflect different organizational structures. An example is that within a business, you have different departments to which you apply distinct Azure subscription policies. This billing model allows you to manage and control access to the resources that users provision with specific subscriptions.
- You can create additional subscriptions to separate:
    * Environments: e.g. dev, testing and production env.
    * Organizational structures: You can create subscriptions to reflect different organizational structures. 
    * Billing: You can create additional subscriptions for billing purposes, because costs are first aggregated at the subscription level.

### Azure management groups
- Azure management groups provide a level of scope above subscriptions. 
- You organize subscriptions into management groups and apply governance conditions to these groups. All subscriptions within a management group automatically inherit the conditions applied to the management group, the same way that resource groups inherit settings from subscriptions and resources inherit from resource groups.

- **Examples of Management group, subscriptions, and resource group hierarchy**
    - Create a hierarchy that applies a policy. You could limit VM locations to the US West Region in a group called Production. This policy will inherit onto all the subscriptions that are descendants of that management group and will apply to all VMs under those subscriptions. This security policy can't be altered by the resource or subscription owner, which allows for improved governance.
    - Provide user access to multiple subscriptions. By moving multiple subscriptions under a management group, you can create one Azure role-based access control (Azure RBAC) assignment on the management group. Assigning Azure RBAC at the management group level means that all sub-management groups, subscriptions, resource groups, and resources underneath that management group would also inherit those permissions. One assignment on the management group can enable users to have access to everything they need instead of scripting Azure RBAC over different subscriptions.
![alt text](https://github.com/viviensiu/Azure/blob/main/images/management-groups-subscriptions.png)
- Important notes about management group:
    * 10,000 management groups can be supported in a single directory.
    * A management group tree can support up to six levels of depth. This limit doesn't include the root level or the subscription level.
    * Each management group and subscription can support only one parent.

### Summary
In this module, you learned about the physical and management structure of Microsoft Azure. You were introduced to the relationship between datacenters, availability zones, and regions. You explored how the infrastructure supports the benefits of the cloud, such as high availability and reliability. You also learned about the management infrastructure of Azure. You explored how resources and resource groups are related, and how subscriptions and management groups can help manage resources.