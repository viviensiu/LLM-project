## Microsoft Azure Fundamentals: Describe features and tools for managing and deploying Azure resources

### Azure Portal
* Web-based, unified console that provides an alternative to CLI. You can: 
    * Manage your Azure subscription by using a graphical user interface. 
    * Build, manage, and monitor everything from simple web apps to complex cloud deployments.
    * Create custom dashboards for an organized view of resources.
    * Configure accessibility options for an optimal experience.
* Designed for resiliency and continuous availability. It maintains a presence in every Azure datacenter which makes the Azure portal resilient to individual datacenter failures and avoids network slowdowns by being close to users. 
* The Azure portal updates continuously and **requires no downtime** for maintenance activities.

### Azure Cloud Shell
* Browser-based shell tool that allows you to create, configure, and manage Azure resources.
* Supports both Azure PowerShell and the Azure CLI which is a Bash shell.
* Access it here in the portal:
![alt text](https://github.com/viviensiu/Azure/blob/main/images/cloud-shell-icon.png) 
* Its features are:
    * Browser-based shell experience with no local installation or configuration required.
    * Authenticated to your Azure credentials, so when you log in, it inherently knows who you are and what permissions you have.
    * You choose the shell you’re most familiar with since it supports both Azure PowerShell and the Azure CLI.

### Azure PowerShell
* A shell with which developers, DevOps, and IT professionals can run commands called command-lets (cmdlets). These commands call the Azure REST API to perform management tasks in Azure. Cmdlets can be run independently to handle one-off changes, or they may be combined to help orchestrate complex actions such as:
    * The routine setup, teardown, and maintenance of a single resource or multiple connected resources.
    * The deployment of an entire infrastructure, which might contain dozens or hundreds of resources, from imperative code.
* Capturing the commands in a script makes the process repeatable and automatable.
* In addition to be available via Azure Cloud Shell, you can install and configure Azure PowerShell on Windows, Linux, and Mac platforms.

### Azure CLI 
* Uses Bash commands.
* Provides the same benefits of handling discrete tasks or orchestrating complex operations through code. 
* Also installable on Windows, Linux, and Mac platforms, as well as through Azure Cloud Shell.

### Azure ARC
* Purpose: A multi-cloud and on-premises management platform that simplifies governance and management.
* In utilizing Azure Resource Manager (ARM), Arc lets you extend your Azure compliance and monitoring to your hybrid and multi-cloud configurations. 
* Provides a centralized, unified way to:
    * Manage your entire environment together by projecting your existing non-Azure resources into ARM.
    * Manage multi-cloud and hybrid VMs, Kubernetes clusters, and databases as if they are running in Azure.
    * Use familiar Azure services and management capabilities, regardless of where they live.
    * Continue using traditional ITOps while introducing DevOps practices to support new cloud and native patterns in your environment.
    * Configure custom locations as an abstraction layer on top of Azure Arc-enabled Kubernetes clusters and cluster extensions. 
* Allows you to manage the following resource types hosted outside of Azure:
    * Servers
    * Kubernetes clusters
    * Azure data services
    * SQL Server
    * Virtual machines (preview)

### Azure Resource Manager (ARM) 
* Deployment and management service for Azure. Provides a management layer that enables you to create/update/delete resources in your Azure account. Anytime you do anything with your Azure resources, ARM is involved.
* ARM authenticates and authorizes the request from any Azure tools, APIs, or SDKs. Then, ARM sends the request to the Azure service, which takes the requested action.
* Benefits:
    * Manage your infrastructure through declarative templates rather than scripts. A **Resource Manager template** is a JSON file that defines what you want to deploy to Azure.
    * Deploy, manage, and monitor all the resources for your solution as a group, rather than handling these resources individually.
    * Re-deploy your solution throughout the development life-cycle and have confidence your resources are deployed in a consistent state.
    * Define the dependencies between resources, so they're deployed in the correct order.
    * Apply access control to all services because RBAC is natively integrated into the management platform.
    * Apply tags to resources to logically organize all the resources in your subscription.
    * Clarify your organization's billing by viewing costs for a group of resources that share the same tag.

### Infrastructure as code (IaC)
* A concept where you manage your infrastructure as lines of code. You can use the IaC concept to manage entire deployments using repeatable templates and configurations. 
* 2 examples of IaC: ARM templates and Bicep.
* **ARM template**:
    * Declarative JSON format. 
    * Whole deployment code is verified before execution. This ensures that the resources will be created and connected correctly. The template then orchestrates the creation of those resources in parallel. 
    * Needs only to define the desired state and configuration of each resource in the ARM template, and the template does the rest.
    * Can even execute PowerShell and Bash scripts before or after the resource has been set up.
* Benefits of ARM templates:
    * **Declarative syntax**: ARM templates allow you to create and deploy an entire Azure infrastructure declaratively. Declarative syntax means you declare what you want to deploy but don’t need to write the actual programming commands and sequence to deploy the resources.
    * **Repeatable results**: Repeatedly deploy your infrastructure throughout the development lifecycle in a consistent manner. You can use the same ARM template to deploy multiple dev/test environments, knowing that all the environments are the same.
    * **Orchestration**: ARM orchestrates the deployment of interdependent resources, so they're created in the correct order. When possible, Azure Resource Manager deploys resources in parallel. You deploy the template through one command instead of multiple imperative commands.
    * **Modular files**: You can break your templates into smaller, reusable components and link them together at deployment time. You can also nest one template inside another template. 
    * **Extensibility**: With deployment scripts, you can add PowerShell or Bash scripts to your templates. The deployment scripts extend your ability to set up resources during deployment. A script can be included in the template or stored in an external source and referenced in the template. Deployment scripts give you the ability to complete your end-to-end environment setup in a single ARM template.
* **Bicep**:
    * A Bicep file defines the infrastructure and configuration. Also written in JSON.
* Benefits of Bicep file:
    * **Support for all resource types and API versions**: Immediately supports all preview and GA versions for Azure services. You don't have to wait for tools to be updated before using the new services.
    * **Simple syntax**: Compared to the equivalent JSON template, Bicep files are more concise and easier to read. Requires no previous knowledge of programming languages. Syntax is declarative and specifies which resources and resource properties you want to deploy.
    * **Repeatable results**: Repeatedly deploy your infrastructure throughout the development lifecycle in a consistent manner. Bicep files are idempotent, which means you can deploy the same file many times and get the same resource types in the same state. You can develop one file that represents the desired state, rather than developing lots of separate files to represent updates.
    * **Orchestration**: ARM orchestrates the deployment of interdependent resources so they're created in the correct order. When possible, Resource Manager deploys resources in parallel. You deploy the file through one command instead of through multiple imperative commands.
    * **Modularity**: You can break your Bicep code into manageable parts by using modules. The module deploys a set of related resources. Modules enable you to reuse code and simplify development. Add the module to a Bicep file anytime you need to deploy those resources. 

### Summary
In this module, you were introduced to features and tools for managing and deploying Azure resources. You learned about the Azure portal (a graphic interface for managing Azure resources), command line, and scripting tools that help deploy or configure resources. You also learned about Azure services that help you manage your on-premises and multicloud environment from Azure.