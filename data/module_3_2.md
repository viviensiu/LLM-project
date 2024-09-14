## Microsoft Azure Fundamentals: Describe Azure management and governance

### Microsoft Purview
* A family of **data governance, risk, and compliance solutions** that provides a single, unified view into your data. 
* Brings insights about your on-premises, multicloud, and software-as-a-service (SaaS) data together.
* You can stay up-to-date on your data landscape thanks to:
    * Automated data discovery.
    * Sensitive data classification.
    * End-to-end data lineage.
* 2 main solution areas comprise Microsoft Purview: 
    * Risk and compliance  
    * Unified data governance.
![alt text](https://github.com/viviensiu/Azure/blob/main/images/purview-solution-areas.png)
* **Microsoft Purview risk and compliance solutions**:
    * Core component: MS 365. Uses M365 services such as Microsoft Teams, OneDrive, and Exchange to help manage and monitor your data. 
* The data monitoring and management helps to:
    * Protect sensitive data across clouds, apps, and devices.
    * Identify data risks and manage regulatory compliance requirements.
    * Get started with regulatory compliance.
* **Microsoft Purview unified data governance**: Helps organization to manage data stored in Azure, SQL and Hive databases, locally, and even in other clouds like Amazon S3. It works by:
    * Create an up-to-date map of your entire data estate that includes data classification and end-to-end lineage.
    * Identify where sensitive data is stored in your estate.
    * Create a secure environment for data consumers to find valuable data.
    * Generate insights about how your data is stored and used.
    * Manage access to the data in your estate securely and at scale.

### Azure Policy
* A service that enables create, assign, and manage policies that control or audit your resources. These policies enforce different rules across resource configurations so that those configurations stay compliant with corporate standards.
* You can define individual policies and groups of related policies, known as initiatives. 
* Azure Policy evaluates and highlights existing resources that are non-compliant, and prevents non-compliant resources from being created.
* You can set policies at different levels: specific resource, resource group, subscription, and so on. These policies are inherited by child groupings.
* Comes with built-in policy and initiative definitions for Storage, Networking, Compute, Security Center, and Monitoring. also It also evaluates and monitors all current VMs in your environment, including VMs that were created before the policy was created. 
* In some cases, Azure Policy can **automatically remediate** noncompliant resources and configurations to ensure the integrity of the state of the resources. E.g., if all resources in a resource group should be tagged, Azure Policy will automatically apply that tag if it is missing. However, you still retain full control of your environment. If you have a specific resource that you don’t want Azure Policy to automatically fix, you can flag that resource as an exception.
* Also integrates with Azure DevOps by applying any CI/CD pipeline policies that pertain to the pre-deployment and post-deployment phases of your applications.
* **Azure Policy initiative**: A way of grouping related policies together. Contains all of the policy definitions under the initiative definition to track compliance state for a larger goal. E.g., Enable Monitoring initiative in Azure Security Center. Its goal is to monitor all available security recommendations for all Azure resource types in Azure Security Center. Enable Monitoring contains over 100 separate policy definitions.
* Under Azure Policy initiative, the following policy definitions are included in Security Center:
    * Monitor unencrypted SQL Database: Monitors for unencrypted SQL databases and servers.
    * Monitor OS vulnerabilities: Monitors servers that don't satisfy the configured OS vulnerability baseline.
    * Monitor missing Endpoint Protection: Monitors for servers that don't have an installed endpoint protection agent.

### Resource Locks
* Purpose: Prevent resources from being deleted or updated even by people with RBAC, depending on the type of lock. Can be applied to individual resources, resource groups, or even an entire subscription. Resource locks are inherited.
* 2 types of resource locks:
    * Delete: Authorized users can still read and modify a resource, but they can't delete the resource.
    * ReadOnly: authorized users can read a resource, but they can't delete or update the resource. Applying this lock is similar to restricting all authorized users to the permissions granted by the Reader role.
* Managing resource locks: via Azure portal, PowerShell, the Azure CLI, or from an Azure Resource Manager template. To view/add/delete locks in the Azure portal, go to the Settings section of any resource's Settings pane in the Azure portal and click on "Lock":
![alt text](https://github.com/viviensiu/Azure/blob/main/images/resource-lock.png)
* Resource locks apply regardless of RBAC permissions. Hence to modify/delete a locked resource, you must first remove the lock. After you remove the lock, you can apply any action you have permissions to perform based on your RBAC. Even if you're an owner of the resource, you must still remove the lock before you can perform the blocked activity.

### Microsoft Service Trust Portal
* A portal that provides access to various content, tools, and other resources about Microsoft security, privacy, and compliance practices.
* Contains details about Microsoft's implementation of controls and processes that protect our cloud services and the customer data therein. 
* To access some of the resources within, you must sign in as an authenticated user with your Microsoft cloud services account (Microsoft Entra organization account). You'll need to review and accept the Microsoft non-disclosure agreement for compliance materials.
![alt text](https://github.com/viviensiu/Azure/blob/main/images/service-trust-portal.png)
* The [Service Trust Portal](https://servicetrust.microsoft.com/) features and content are accessible from the main menu. The categories on the main menu are:
    * **Service Trust Portal**: Provides quick access hyperlink to return to the home page.
    * **My Library**: Lets you save (or pin) documents to quickly access them on your My Library page. Can also set up notifications when documents in your My Library are updated.
    * **All Documents**: Single landing place for documents on the service trust portal. From All Documents, you can pin documents to have them show up in your My Library.
* **NOTE**: Service Trust Portal reports and documents are available to download for at least 12 months after publishing or until a new version of document becomes available.

### Summary 
In this module, you learned about some of the features and tools you can use to help with governance of your Azure environment. You also learned about tools you can use to help keep resources in compliance with corporate or regulatory requirements.