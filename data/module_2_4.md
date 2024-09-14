## Microsoft Azure Fundamentals: Describe Azure identity, access, and security

### Azure directory services
* Microsoft Entra ID and Microsoft Entra Domain Services.

### Microsoft Entra ID
* Microsoft Entra ID: Cloud-based identity and access management (IAM) service.
* Active Directory: On-premise Window server's identity and access management (IAM) service.
* Could also help to maintain your on-premises Active Directory deployment. This works by connecting Active Directory with Microsoft Entra ID, and Microsoft helps to detect suspicious sign-in attempts, e.g. from unknown locations or devices at no extra cost (AD doesn't monitor sign-in attempts).
* **Note**: Having both AD and Entra ID means that you need to maintain 2 identity sets. However, you could connect AD and Entra ID to maintain a consistent identity experience, such as connect them using Microsoft Entra Connect.
* Microsoft Entra Connect: synchronizes user identities between on-premises Active Directory and Microsoft Entra ID, to allow using features like SSO, multifactor authentication, and self-service password reset under both systems.
* Microsoft Entra ID is for:
    * IT administrators: Control access to applications and resources based on their business requirements.
    * App developers: Provide a standards-based approach for adding functionality to applications that they build, such as adding SSO functionality to an app or enabling an app to work with a user's existing credentials.
    * Users: Manage identities and maintenance like self-service password reset.
    * Online service subscribers: Account authentication for subscribers of Microsoft 365, Microsoft Office 365, Azure, and Microsoft Dynamics CRM Online.
* Microsoft Entra ID provides services such as:
    * Authentication: Verifying identity, self-service password reset, multifactor authentication, a custom list of banned passwords, and smart lockout services.
    * Single sign-on (SSO).
    * Application management: Manage your cloud and on-premises apps. Features like Application Proxy, SaaS apps, the My Apps portal, and single sign-on provide a better user experience.
    * Device management: Supports the registration of devices. Registration enables devices to be managed through tools like Microsoft Intune. It also allows for device-based Conditional Access policies to restrict access attempts to only those coming from known devices, regardless of the requesting user account.

### Microsoft Entra Domain Services
* A service that provides managed domain services such as domain join, group policy, lightweight directory access protocol (LDAP), and Kerberos/NTLM authentication. 
* Benefit of domain services without the need to deploy, manage, and patch domain controllers (DCs) in the cloud.
* Why do you need this? To run legacy applications in the cloud that can't use modern authentication methods, or where you don't want directory lookups to always go back to an on-premises AD DS environment. 
* Integrates with your existing Microsoft Entra tenant, so users can sign into services and applications connected to the managed domain using their existing credentials. 
* How does MEDS work:
    * Create a MEDS managed domain and define a unique namespace to be the domain name.
    * 2 Windows Server domain controllers are then deployed into your selected Azure region as a replica set. The DCs are managed by Azure as part of the managed domain.
* **Information synchronization**:
    * One-way sync. from Microsoft Entra ID to Microsoft Entra Domain Services. Resources created directly inside MEDS are NOT sync back to Entra ID.
    * In a hybrid environment with an on-premises AD DS environment, Microsoft Entra Connect synchronizes identity information with Microsoft Entra ID (bi-directional), which is then synchronized to the managed domain (uni-directional). See image below:
    ![alt text](https://github.com/viviensiu/Azure/blob/main/images/azure-active-directory-sync-topology.png)

### Azure authentication method
* Security v.s. Convenience:
![alt text](https://github.com/viviensiu/Azure/blob/main/images/passwordless-convenience-security.png)

### Single Sign-On (SSO)
* Enables a user to sign in one time and use that credential to access multiple resources and applications from different providers, where these providers must trust the initial authenticator.
* **Note**: SSO is only as secure as the initial authenticator because the subsequent connections are all based on the security of the initial authenticator.
* Benefits:
    * Greatly reduces the effort needed to change or disable accounts.
    * Easier for users to manage their identities.
    * Easier for IT to manage users: account lockouts, password reset requests, disabling user identities.

### Multifactor authentication
* Process of prompting a user for an extra form (or factor) of identification during the sign-in process.
* Additional security for your identities by requiring two or more elements to fully authenticate, elements such as:
    * Something the user knows – this might be a challenge question.
    * Something the user has – this might be a code that's sent to the user's mobile phone.
    * Something the user is – this is typically some sort of biometric property, such as a fingerprint or face scan.
* Microsoft Entra multifactor authentication: Enables users to choose an additional form of authentication during sign-in, such as a phone call or mobile app notification.

### Passwordless authentication 
* Password is removed and replaced with something you have (e.g. your computer), plus something you are, or something you know.
* Needs to be set up on a device before it can work. Once enrolled, you can be authenticated without using a password by providing something you know or are (such as a PIN or fingerprint).
* Microsoft global Azure and Azure Government offer 3 passwordless authentication options that integrate with Microsoft Entra ID:
    * **Windows Hello for Business**: For those with designated Windows PC. The biometric and PIN credentials are directly tied to the PC, which prevents access from anyone other than the owner. Also supports public key infrastructure (PKI) integration and SSO.
    * **Microsoft Authenticator app**: Phone app. Sign-in by getting a notification to their phone, match a number displayed on the screen to the one on their phone, and then using their biometric (touch or face) or PIN to confirm.
    * **FIDO2 (Fast IDentity Online) security keys**: Unphishable standards-based passwordless authentication method that can come in any form factor. Allows sign-in by using an external security key or a platform key built into a device. Users can register and then select a FIDO2 security key at the sign-in interface as their main means of authentication. These FIDO2 security keys are typically USB devices, but could also use Bluetooth or NFC. 

### Azure External Identities
* **Microsoft Entra External ID** 
    * Ways you can securely interact with users outside of your organization to share your resources with them while you define how your internal users can access external organisations.
![alt text](https://github.com/viviensiu/Azure/blob/main/images/azure-active-directory-external-identities.png)
* 3 capabilities of External ID (you can use more than one):
    * **Business to business (B2B) collaboration**: Allow external users to use their preferred identity to sign-in to your Microsoft applications or other enterprise applications (SaaS apps, custom-developed apps, etc.). B2B users are represented in your directory, typically as guest users.
    * **B2B direct connect**: A mutual, two-way trust with another Microsoft Entra organization for seamless collaboration. Currently supports Teams shared channels, enabling external users to access your resources from their Teams instances. Not represented in your directory, visible from within the Teams shared channel and can be monitored in Teams admin center reports.
    * **Microsoft Azure AD business to customer (B2C)**: Publish modern SaaS apps or custom-developed apps (excluding Microsoft apps) to consumers and customers, while using Azure AD B2C for identity and access management.
* With Microsoft Entra ID, you can use the Microsoft Entra B2B feature. Guest users from other tenants can be invited by administrators or by other users. This capability also applies to social identities such as Microsoft accounts.
* To ensure appropriate access, a access review can be done based on suggestions from Microsoft Entra ID. When an access review is finished, you can then make changes and remove access for guests who no longer need it.

### Azure Conditional Access 
* A tool that Microsoft Entra ID uses to allow (or deny) access to resources based on identity signals.
* During sign-in, Conditional Access collects signals from the user, makes decisions based on those signals, and then enforces that decision by allowing or denying the access request or challenging for a multifactor authentication response.
* Signals: User's location, the user's device, or the application they try to access.
* Decision: Allow full access if it's a usual location. If the user is signing in from an unusual/high risk location, then block access or grant after the user provides a second form of authentication.
* Enforcement: Action that carries out the decision.
![alt text](https://github.com/viviensiu/Azure/blob/main/images/conditional-access.png)
* Conditional Access is useful when:
    * Require multifactor authentication (MFA) to access an application depending on the requester’s role, location, or network.
    * Require access to services only through approved client applications. 
    * Require users to access your application only from managed devices.
    * Block access from untrusted sources, such as access from unknown or unexpected locations.

### Azure role-based access control (Azure RBAC)
* The principle of least privilege says you should only grant access up to the level needed to complete a task. 
* Azure RBAC provides built-in roles or you can define your own roles. Each role has an associated set of access permissions that relate to that role. When you assign individuals or groups to one or more roles, they receive all the associated access permissions.
* RBAC is applied to a scope (resource or set of resources that this access applies to). Scopes include:
    * A management group (a collection of multiple subscriptions).
    * A single subscription.
    * A resource group.
    * A single resource.
* The following diagram shows the relationship between roles and scopes. A management group, subscription, or resource group might be given the role of owner, so they have increased control and authority. An observer, who isn't expected to make any updates, might be given a role of Reader for the same scope, enabling them to review or observe the management group, subscription, or resource group.
![alt text](https://github.com/viviensiu/Azure/blob/main/images/role-based-access-scope.png)
* Azure RBAC is hierarchical, in that when you grant access at a parent scope, those permissions are inherited by all child scopes.
* Azure RBAC is enforced on any action that's initiated against an Azure resource that passes through Azure Resource Manager. You typically access Resource Manager from the Azure portal, Azure Cloud Shell, Azure PowerShell, and the Azure CLI. 
* **Note**: Azure RBAC doesn't enforce access permissions at the application or data level. 
* Uses an allow model: When you're assigned a role, Azure RBAC allows you to perform actions within the scope of that role. If one role assignment grants you read permissions to a resource group and a different role assignment grants you write permissions to the same resource group, you have both read and write permissions on that resource group.

### Zero Trust Model
* A security model that assumes the worst case scenario and protects resources with that expectation. 
* Based on these guiding principles:
    * Verify explicitly: Always authenticate and authorize based on all available data points.
    * Use least privilege access: Limit user access with Just-In-Time and Just-Enough-Access (JIT/JEA), risk-based adaptive policies, and data protection.
    * Assume breach: Minimize blast radius and segment access. Verify end-to-end encryption. Use analytics to get visibility, drive threat detection, and improve defenses.
* Traditional networks adopts a location-based access by assuming that everything within the secured network is safe. Zero Trust flips that assumption and grants access based on authentication rather than location.
![alt text](https://github.com/viviensiu/Azure/blob/main/images/zero-trust.png)

### Defense-in-depth
* Objective: Protect information and prevent it from being stolen by unauthorized personnel.
* Strategies: Uses a series of mechanisms to slow the advance of an attack that aims at acquiring unauthorized access to data. 
* Layers of defense-in-depth: ![alt text](https://github.com/viviensiu/Azure/blob/main/images/defense-depth.png)
* Removes reliance on single layer of protection, slows attack and alerts security authorities.
* **Physical security layer**: 
    * First line of defense to protect computing hardware in the datacenter. Secures access to buildings and controls access to computing hardware within the datacenter.
* **Identity and access layer**: 
    * Control access to infrastructure and change control.
    * Use single sign-on (SSO) and multifactor authentication.
    * Audit events and changes.
* **Perimeter layer**: Defense against network-based attacks. 
    * Uses DDoS protection to filter large-scale attacks before they can cause a denial of service for users.
    * Use perimeter firewalls to identify and alert on malicious attacks against your network.
* **Network layer**: Limits network connectivity to reduce risk of attack spreading to other systems.
    * Limit communication between resources.
    * Deny by default.
    * Restrict inbound internet access and limit outbound access where appropriate.
    * Implement secure connectivity to on-premises networks.
* **Compute layer**: Making sure compute resources are secure.
    * Secures access to virtual machines.
    * Implement endpoint protection on devices and keep systems patched and current.
* **Application layer**: 
    * Ensure that applications are secure and free of vulnerabilities.
    * Store sensitive application secrets in a secure storage medium.
    * Make security a design requirement for all application development.
* **Data layer**: Controls access to business and customer data that you need to protect. Often, regulatory requirements dictate the controls and processes that must be in place to ensure the confidentiality, integrity, and availability of the data. In almost all cases, attackers are after data:
    * Stored in a database.
    * Stored on disk inside virtual machines.
    * Stored in software as a service (SaaS) applications, such as Office 365.
    * Managed through cloud storage.

### Microsoft Defender for Cloud
* A monitoring tool for security posture management and threat protection. It monitors cloud, on-premises, hybrid, and multi-cloud environments to provide guidance and notifications aimed at strengthening your security posture.
* An Azure-native service which already monitors and protect Azure services without deployment.
* Deploys a Log Analytics agent to gather security-related data. This is direct on Azure. For hybrid and multi-cloud, Microsoft Defender plans are extended to non Azure machines with the help of Azure Arc. Cloud security posture management (CSPM) features are extended to multi-cloud machines without the need for any agents.
* **Azure-native protections**:
    * Azure PaaS services: Detect threats targeting Azure services. You can also perform anomaly detection on your Azure activity logs using the native integration with Microsoft Defender for Cloud Apps (formerly known as Microsoft Cloud App Security).
    * Azure data services: Help you automatically classify your data in Azure SQL. You can also get assessments for potential vulnerabilities across Azure SQL and Storage services, and recommendations for how to mitigate them.
    * Networks: Helps limit exposure to brute force attacks. By reducing access to VM ports, using the just-in-time VM access, you can harden your network by preventing unnecessary access. You can set secure access policies on selected ports, for only authorized users, allowed source IP address ranges or IP addresses, and for a limited amount of time.
* Defend your hybrid resources:
    * Add Defender for Cloud capabilities to your hybrid cloud environment to protect your non-Azure servers.
    * For on-premises machines, deploy Azure Arc and enable Defender for Cloud's enhanced security features.
* Defend resources running on other clouds (e.g. AWS and GCP):
    * Defender for Cloud's CSPM features extend to your AWS resources. This agentless plan assesses your AWS resources according to AWS-specific security recommendations, and includes the results in the secure score. The resources will also be assessed for compliance with built-in standards specific to AWS. Defender for Cloud's asset inventory page is a multi-cloud enabled feature helping you manage your AWS resources alongside your Azure resources.
    * Microsoft Defender for Containers extends its container threat detection and advanced defenses to your Amazon EKS Linux clusters.
    * Microsoft Defender for Servers brings threat detection and advanced defenses to your Windows and Linux EC2 instances.

* **Assess, Secure, and Defend**: 3 vital needs as you manage the security of your resources and workloads in the cloud and on-premises:
![alt text](https://github.com/viviensiu/Azure/blob/main/images/assess-secure-defend.png)
* Continuously assess:
    * Vulnerability assessment solutions for VMs, container registries, and SQL servers.
    * Microsoft Defender for servers integration with Microsoft Defender for Endpoint provides vulnerability findings from Microsoft threat and vulnerability management.
    * Between these assessment tools you’ll have regular, detailed vulnerability scans that cover your compute, data, and infrastructure. You can review and respond to the results of these scans all from within Defender for Cloud.
* Secure:
    * Policies in Defender for Cloud are built on top of Azure Policy controls. In Defender for Cloud, you can set your policies to run on management groups, across subscriptions, and even for a whole tenant.
    * Constantly assess if new resources are configured according to security best practices. If not, they're flagged and you get a prioritized list of recommendations for what you need to fix.
    * The list of recommendations is enabled and supported by the Azure Security Benchmark. This Microsoft-authored, Azure-specific, benchmark provides a set of guidelines for security and compliance best practices based on common compliance frameworks. In this way, Defender for Cloud enables you not just to set security policies, but to apply secure configuration standards across your resources.
    * Defender for Cloud groups the recommendations into security controls and adds a secure score value to each control. The secure score gives you an at-a-glance indicator of the health of your security posture, while the controls give you a working list of things to consider to improve your security score and your overall security posture. ![alt text](https://github.com/viviensiu/Azure/blob/main/images/defender-for-cloud.png)
* Defend:
    * Defender for Cloud provides security alert which: Describe details of the affected resources. Suggest remediation steps. Provide, in some cases, an option to trigger a logic app in response.
    * Alerts can be exported.
    * Defender for Cloud's threat protection includes fusion kill-chain analysis, which automatically correlates alerts in your environment based on cyber kill-chain analysis, to help you better understand the full story of an attack campaign, where it started, and what kind of impact it had on your resources.
    * Advanced threat protection: Securing the management ports of your VMs with just-in-time access. Adaptive application controls to create allowlists for what apps should and shouldn't run on your machines.

### Summary
In this module, you learned about Azure identity, access, and security services and tools. You covered authentication methods, including which ones are more secure. You learned about restricting access based on a role to help create a more secure environment. And, you learned about the Defense In Depth and Zero Trust models.
