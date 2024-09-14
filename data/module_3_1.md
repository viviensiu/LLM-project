## Microsoft Azure Fundamentals: Describe cost management in Azure

### Factors that affect costs in Azure
* Azure shifts development costs from the capital expense (CapEx) to an operational expense (OpEx) of renting infrastructure as you need it, whether it’s compute, storage, networking, and so on. TOpEx cost can be impacted by many factors such as:
    * Resource type
    * Consumption
    * Maintenance
    * Geography
    * Subscription type
    * Azure Marketplace
* **Resource type**: Its costs are influenced by the type of resource, the settings of the resource and the Azure region. When you provision an Azure resource, Azure creates metered instances for that resource. The meters track the resources' usage and generate a usage record that is used to calculate your bill.
    * Example of blob storage: Changing its settings and region produce different costs. ![alt text](https://github.com/viviensiu/Azure/blob/main/images/blob-storage.png)
    * Example of a VM: Using different OS licenses, hardwares e.g. processor, num. of CPUs, storage and network results in different costs. ![alt text](https://github.com/viviensiu/Azure/blob/main/images/virtual-machine-settings.png)
* **Consumption**: Generally you pay-as-you-go for what you use, so it fluctuates around usage. However you could also commit to using a set amount of cloud resources in advance and receiving discounts up to 72% on those “reserved” resources. With the back-up of pay-as-you-go, if you see a sudden surge in demand that eclipses what you’ve pre-reserved, you just pay for the additional resources in excess of your reservation. This model allows you to recognize significant savings on reliable, consistent workloads while also having the flexibility to rapidly increase your cloud footprint as the need arises.
* **Maintenance**: When you deprovision some resource like a VM, the accompanying resources such as network and storage may not deprovision at the same time. By keeping an eye on your resources and making sure you’re not keeping around resources that are no longer needed, you can help control cloud costs.
* **Geography**: There are global pricing difference due to the cost of power, labor, taxes, and fees vary depending on the location. Hence Azure resources can differ in costs to deploy depending on the region. Network traffic is also impacted based on geography. For example, it’s less expensive to move information within Europe than to move information from Europe to Asia or South America.
* **Network Traffic**: Billing zones are a factor in the costs of some services, as data transfer pricing (inbound and outbound) are based on zones. A zone is a geographical grouping of Azure regions for billing purposes.
* **Subscription type**: Costs are affected by the usage allowances in your subscription, e.g. a free trial subscription offers access to a number of Azure products that are free for 12 months. It also includes $200 credit to spend within your first 30 days of sign-up. You'll get access to more than 25 products that are always free (based on resource and region availability).
* **Azure Marketplace**: A place to purchase Azure-based solutions and services from third-party vendors. You may pay for not only the Azure services that you’re using, but also the services or expertise of the third-party vendor. Billing structures are set by the vendor. These solutions are certified and compliant with Azure policies and standards. Certification policies may vary based on the service or solution type and Azure service involved.

### Pricing and Total Cost of Ownership (TCO) calculators
* **Pricing calculator**: To estimate the cost of any provisioned resources, including compute, storage, and associated network costs. You can even account for different storage options like storage type, access tier, and redundancy. Nothing is provisioned when you add resources to the pricing calculator, and you won't be charged for any services you select.
![alt text](https://github.com/viviensiu/Azure/blob/main/images/price-calculator.png)
* **TCO calculator**: Helps compare the costs for running an on-premises infrastructure compared to an Azure Cloud infrastructure.  You enter your current infrastructure configuration, including servers, databases, storage, and outbound network traffic, plus power and IT labor costs. The TCO calculator then compares the anticipated costs for your current environment with the same Azure environment.
![alt text](https://github.com/viviensiu/Azure/blob/main/images/total-cost-ownership.png)

### Microsoft Cost Management tool
* **Cost Management**: Service to quickly check Azure resource costs, create alerts based on resource spend, and create budgets that can be used to automate management of resources. This helps to stay aware of your resource costs and prevent surprise costs.
* **Cost analysis**: Subset of Cost Management to provide a quick visual for your Azure costs. You can quickly view the total cost in a variety of different ways, including by billing cycle, region, resource, and so on. You can view aggregated costs by organization to understand where costs are accrued and to identify spending trends. And you can see accumulated costs over time to estimate monthly, quarterly, or even yearly cost trends against a budget.
![alt text](https://github.com/viviensiu/Azure/blob/main/images/cost-analysis.png)
* **Cost alerts** : To quickly check on all of the different alert types that may show up in the Cost Management service. Whenever an alert is generated, it appears in cost alerts. An alert email is also sent to the people in the alert recipients list. 3 types of alerts:
    * **Budget alerts**: In the Azure portal, budgets are defined by cost while in Azure Consumption API, budgets are defined by cost or by consumption usage. Budget alerts support both cost-based and usage-based budgets. Alerts are generated automatically when usage or cost reaches or exceeds the amount defined in the alert condition. 
    * **Credit alerts**: alerts you when your Azure credit monetary commitments are consumed (monetary commitments are for organizations with Enterprise Agreements (EAs)). Credit alerts are generated automatically at 90% and at 100% of your Azure credit balance to cost alert and email account owners. 
    * **Department spending quota alerts**: Notify you when department spending reaches a fixed threshold (e.g. 50% or 75%) of the spending quota (configured in the EA portal). Email dept owners.
* **Budget**: Spending limit for Azure. Can be set based on subscription/resource group/service type/others. Comes with a budget alert, which shows up in the cost alerts area. If configured, budget alerts will also send an email notification that a budget alert threshold has been triggered. Advanced use of budgets: Enables budget conditions to trigger automation that suspends/ modifies resources once the trigger condition has occurred.

### Tags
* Methods to organise related resources:
    * Place in own subscriptions.
    * Resource groups.
    * Resource tags.
* Resource tags provide extra information, or metadata, about your resources. This metadata is useful for:
    * **Resource management**: Enable you to locate and act on associated resources (specific workloads, environments, business units, and owners).
    * **Cost management and optimization**: Enable you to group resources to report on costs, allocate internal cost centers, track budgets, and forecast estimated cost.
    * **Operations management**: Enable you to group resources according to business criticality/availability. Helps you formulate service-level agreements (SLAs, an uptime or performance guarantee).
    * **Security**: Enable you to classify data by its security level, such as public or confidential.
    Governance and regulatory compliance Tags enable you to identify resources that align with governance or regulatory compliance requirements, such as ISO 27001. Tags can also be part of your standards enforcement efforts. For example, you might require that all resources be tagged with an owner or department name.
    * **Workload optimization and automation**: Help you visualize all of the resources that participate in complex deployments. For example, you might tag a resource with its associated workload or application name and use software such as Azure DevOps to perform automated tasks on those resources.
* Tag management:
    * Add, modify, or delete resource tags through Windows PowerShell, the Azure CLI, Azure Resource Manager templates, the REST API, or the Azure portal.
    * Use Azure Policy to enforce tagging rules and conventions.
    * Define rules that reapply tags that have been removed.
    * Resources don't inherit tags from subscriptions and resource groups, allowing custom tagging schemas.
* Example of tagging structure:
    * AppName: The name of the application that the resource is part of.
    * CostCenter: The internal cost center code.
    * Owner: The name of the business owner who's responsible for the resource.
    * Environment: An environment name, such as "Prod", "Dev", or "Test".
    * Impact: How important the resource is to business operations, such as "Mission-critical", "High-impact", or "Low-impact".
* **NOTE**: Tags are optional on resources.

### Summary
In this module, you learned about factors that impact costs in Azure and tools to help you both predict potential costs and monitor and control costs.