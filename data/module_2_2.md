## Microsoft Azure Fundamentals: Describe Azure compute and networking services

### Azure virtual machines
* VM: Provides IaaS in the form of a virtualized server. No hardware maintenance, however you still need to configure, update, and maintain the software.
* VMs are an ideal choice when you need:
    * Total control over the operating system (OS).
    * The ability to run custom software.
    * To use custom hosting configurations.
* An image is a template used to create a VM and may already include an OS and other software, like development tools or web hosting environments.
* You can even create or use an already created image to rapidly provision VMs.

* Scale VMs in Azure
    * Azure can manage the grouping of VMs for you with features such as scale sets and availability sets.
* **Virtual machine scale sets**: 
    * Create and manage a group of identical, load-balanced VMs.
    * Scale sets allow you to centrally manage, configure, and update a large number of VMs in minutes.
    * The number of VM instances can automatically increase or decrease in response to demand, or you can set it to scale based on a defined schedule.
    * Automatically deploy a load balancer.
* **Availability sets**:
    * Ensure that VMs stagger updates and have varied power and network connectivity, preventing you from losing all your VMs with a single network or power failure. 
    * Group VMs in 2 way: update domain and fault domain.
    * Update domain: groups VMs that can be rebooted at the same time. 
    * Fault domain: groups VMs by common power source and network switch. By default, an availability set will split your VMs across up to 3 fault domains. This helps protect against a physical power or networking failure by having VMs in different fault domains.
    * No additional cost for configuring an availability set.

* **Examples of when to use VMs**
    * During testing and development.
    * When running applications in the cloud.
    * When extending your datacenter to the cloud.
    * During disaster recovery.

* **Move to the cloud with VMs**
    * lift and shift by creating an image of the physical server and host it within the VM.

* **VM Resources**
    * Size (purpose, number of processor cores, and amount of RAM)
    * Storage disks (hard disk drives, solid state drives, etc.)
    * Networking (virtual network, public IP address, and port configuration)

### Azure Virtual Desktop
* Desktop and application virtualization service that runs on the cloud. It enables you to use a cloud-hosted version of Windows from any location.
* Works on any devices: Windows, MacOS, iOS, Android from any modern browser.
* Separates OS, apps and data from local hardware and run on remote server instead.
* Windows 10 or Windows 11 Enterprise multi-session, the only Windows client-based operating system that enables multiple concurrent users on a single VM.
* Supports OneNote and Microsoft 365.
* Centralized security management for users' desktops with **Microsoft Entra ID**. You can enable multifactor authentication to secure user sign-ins. You can also secure access to data by assigning granular role-based access controls (RBACs) to users.

### Azure containers
* Enables multiple instances of an application on a single host machine, unlike VM which are limited to a single OS.
* Unlike virtual machines, you don't manage the operating system for a container. It bundles a single app and its dependencies.
* VM virtualise the hardware, while containers virtualise the OS.
* Containers are lightweight and designed to be created, scaled out, and stopped dynamically.
* It can be orchestrated with cluster orchestration.
* **Azure Container Instances**: 
    * PaaS offering.
    * Upload your containers and then the service will run the containers for you.
* **Azure Container Apps**: 
    * PaaS offering and similar to Azure Container Instances.
    * Extra benefits such as the ability to incorporate load balancing and scaling.
* **Azure Kubernetes Service (AKS)**:
    * Container orchestration service. An orchestration service manages the lifecycle of containers. 
* Containers are used to create solutions by using a microservice architecture, where architecture breaks solution into smaller, independent pieces. This allows you to separate portions of your app into logical sections that can be maintained, scaled, or updated independently.

### Azure Functions
* An event-driven, serverless compute option that doesn’t require maintaining virtual machines or containers.
* Key component of serverless computing, can also be used in server env.
* VM and containers are required to be up at all times for an app to function, however, AZ functions wakes up the app when there's event hence it frees up resources when not in use.
* Functions are commonly used when you need to perform work in response to an event (often via a REST request), timer, or message from another Azure service, and when that work can be completed quickly, within seconds or less.
* **Benefits of Azure Function**:
    * Scale automatically based on demand.
    * Runs your code when it's triggered and automatically deallocates resources when the function is finished. Only charged based on the CPU used.
    * Can be either stateless or stateful: Stateless (the default), fresh restart on each event. For Stateful (called Durable Functions), a context is passed through the function to track prior activity.

### Application hosting options
* Other than VM and containers, you could also explore:
* **Azure App Service**: 
    * **HTTP-based service** to build and host web apps, background web jobs, mobile back-ends, and RESTful APIs in the programming language of your choice without managing infrastructure.
    * Supports Windows and Linux.
    * Automated deployments from GitHub, Azure DevOps, or any Git repo to support a continuous deployment model.
    * Deployment and management are integrated into the platform.
    * Endpoints can be secured.
    * Sites can be scaled quickly to handle high traffic loads.
    * The built-in load balancing and traffic manager provide high availability.
    * **Types of web app**: ASP.NET, ASP.NET Core, Java, Ruby, Node.js, PHP, or Python.
    * **API apps**: Full Swagger support and the ability to package and publish your API in Azure Marketplace. API apps can be consumed from any HTTP- or HTTPS-based client.
    * **Web jobs**: Run a program (.exe, Java, PHP, Python, or Node.js) or script (.cmd, .bat, PowerShell, or Bash) either scheduled or triggered.
    * **Mobile app**: Provides a backend for iOS or Android. Store mobile app data in a cloud-based SQL database. Authenticate customers against common social providers. Send push notifications. Execute custom back-end logic in C# or Node.js.there's SDK support for native iOS and Android, Xamarin, and React native apps.

### Azure Virtual Networking
* Azure virtual networks provide the following key networking capabilities:
    * Isolation and segmentation.
    * Internet communications.
    * Communicate between Azure resources.
    * Communicate with on-premises resources.
    * Route network traffic.
    * Filter network traffic.
    * Connect virtual networks.
* Supports both public and private endpoints:
    * Public endpoints have a public IP address and can be accessed from anywhere in the world.
    * Private endpoints exist within a virtual network and have a private IP address from within the address space of that virtual network.

### Network Isolation and Segmentation
* Can create multiple isolated virtual networks.
* Setup: Define a private IP address space by using either public or private IP address ranges. The IP range only exists within the (isolated) virtual network and isn't internet routable. 
* The IP address space can be divided into subnets, each named subnet gets allocated part of the defined address space.
* Name resolution: use name resolution service built into Azure.
* Can use internal or an external DNS server.

### Internet communications
* Enable incoming connections from the internet by: 
    * Public IP address to an Azure resource, 
    * Public load balancer before the resource.

### Communicate between Azure resources
* 2 ways:
    * Virtual networks: For VMs and Azure resources, such as the App Service Environment for Power Apps, Azure Kubernetes Service, and Azure virtual machine scale sets.
    * Service endpoints: For Azure resource types such as Azure SQL databases and storage accounts. This approach enables you to link multiple Azure resources to virtual networks to improve security and provide optimal routing between resources.

### Communicate with on-premises resources
* 3 ways to create a network that spans both your local and cloud environments:
    * Point-to-site VPN connections: From a computer outside your organization back into your corporate network. In this case, the client computer initiates an encrypted VPN connection to connect to the Azure virtual network.
    * Site-to-site VPN: Link your on-premises VPN device or gateway to the Azure VPN gateway in a virtual network. In effect, the devices in Azure can appear as being on the local network. The connection is encrypted and works over the internet.
    * Azure ExpressRoute: Dedicated private connectivity to Azure that doesn't travel over the internet. ExpressRoute is useful for environments where you need greater bandwidth and even higher levels of security.

### Route network traffic
* Default: Routes traffic between subnets on any connected virtual networks, on-premises networks, and the internet.
* Custom control for routing:
    * Route tables: Define rules about how traffic should be directed. You can create custom route tables that control how packets are routed between subnets.
    * Border Gateway Protocol (BGP) works with Azure VPN gateways, Azure Route Server, or Azure ExpressRoute to propagate on-premises BGP routes to Azure virtual networks.

### Filter network traffic
* Network security groups: Azure resources that can contain multiple inbound and outbound security rules.
* Network virtual appliances: Specialized VMs that can be compared to a hardened network appliance. Carries out a particular network function, such as running a firewall or performing wide area network (WAN) optimization.

### Virtual Network Peering
* Allows two virtual networks to connect directly to each other. 
* Network traffic between peered networks is private, and travels on the Microsoft backbone network, never entering the public internet. 
* Enables resources in each virtual network to communicate with each other.
* User-defined routes (UDR): Allows control of the routing tables between subnets within a virtual network or between virtual networks. 

### Virtual private network (VPN)
* Uses an encrypted tunnel within another network.
* Connect two or more trusted private networks to one another over an untrusted network (typically the public internet).
* Traffic is encrypted when travel over untrusted network. 
* **Azure VPN Gateway** instances are deployed in a dedicated subnet of the virtual network and enable the following connectivity:
    * Connect on-premises datacenters to virtual networks through a site-to-site connection.
    * Connect individual devices to virtual networks through a point-to-site connection.
    * Connect virtual networks to other virtual networks through a network-to-network connection.
* **Only one VPN gateway in each virtual network**. One gateway can to connect to multiple locations, including other virtual networks or on-premises datacenters.
* VPN gateway setup: Must specify the type of VPN (policy-based or route-based) to determine which traffic needs encryption. 
    * **Policy-based VPN gateways**: specify statically the IP address of packets that should be encrypted through each tunnel. This type of device evaluates every data packet against those sets of IP addresses to choose the tunnel where that packet is going to be sent through.
    * **Route-based gateways**: IPSec tunnels are modeled as a network interface or virtual tunnel interface. IP routing (static or dynamic routing) decides which one of these tunnel interfaces to use when sending each packet. The preferred connection method for on-premises devices, more resilient to topology changes such as the creation of new subnets.
* Use **Route-based VPN gateway** if you need:
    * Connections between virtual networks
    * Point-to-site connections
    * Multisite connections
    * Coexistence with an **Azure ExpressRoute** gateway
* Method of authentication: Preshared key.

### High-availability Scenarios
* A few ways to maximize the resiliency of your VPN gateway:
    * **Active/standby**: By default, VPN gateways are deployed as two instances in an active/standby configuration. When connections to active instance are interrupted, the failover to standby gateway will take a few seconds (for planned maintenance) or within 90s (for unplanned interruptions).
    * **Active/active**: Assign a unique public IP address to each instance, and create separate tunnels from the on-premises device to each IP address.
    * **ExpressRoute failover**: ExpressRoute circuits have resiliency built in but could be affected by issues on physical cables or outages. A VPN gateway can be a secure failover path for ExpressRoute connections.
    * **Zone-redundant gateways**: VPN gateways and ExpressRoute gateways can be deployed in a zone-redundant configuration for regions that offer availability zones. It physically and logically separates gateways within a region while protecting your on-premises network connectivity to Azure from zone-level failures. Require different gateway SKUs (stock keeping units - i.e. specific version of a resource or service) and use Standard public IP addresses instead of Basic public IP addresses.

### Azure ExpressRoute 
* Lets you extend your on-premises networks into the Microsoft cloud over a private connection, with the help of a ExpressRoute Circuit (connectivity provider).
* **Features and benefits of ExpressRoute**:
    * Connectivity to Microsoft cloud services across all regions in the geopolitical region.
    * Global connectivity to Microsoft services across all regions with the ExpressRoute Global Reach.
    * Dynamic routing between your network and Microsoft via Border Gateway Protocol (BGP).
    * Built-in redundancy in every peering location for higher reliability.
* **Connectivity to Microsoft cloud services**:
    * Microsoft Office 365.
    * Microsoft Dynamics 365.
    * Azure compute services, such as Azure Virtual Machines.
    * Azure cloud services, such as Azure Cosmos DB and Azure Storage.
* **ExpressRoute Global Reach**: Exchange data across your on-premises sites by connecting your ExpressRoute circuits. Example: 2 sites in different regions, both with ExpressRoute circuits connecting them to the Microsoft network, can communicate via ExpressRoute Global Reach without going thru internet.
* **Dynamic routing via Border Gateway Protocol (BGP)**: Exchange routes between on-premises networks and resources running in Azure.
* **Built-in redundancy**: Each connectivity provider uses redundant devices to ensure that connections established with Microsoft are highly available. 

### ExpressRoute connectivity models
* 4 models to connect your on-premises network to the Microsoft cloud:
    * **CloudExchange colocation**: Applies to facilities that're physically colocated at a cloud exchange, where you can request a virtual cross-connect to the Microsoft cloud.
    * **Point-to-point Ethernet connection**: Point-to-point connection to connect your facility to the Microsoft cloud.
    * **Any-to-any connection**: Integrate your wide area network (WAN) with Azure by providing connections to your offices and datacenters.
    * **Directly from ExpressRoute sites**: Connect directly into the Microsoft's global network at a peering location. ExpressRoute Direct provides dual 100 Gbps or 10-Gbps connectivity, which supports Active/Active connectivity at scale.
* **Security considerations**
    * ExpressRoute is a private connection from your on-premises infrastructure to your Azure infrastructure.
    * Even if you have an ExpressRoute connection, DNS queries, certificate revocation list checking, and Azure Content Delivery Network requests are still sent over the public internet.

### Azure DNS 
* Hosting service for DNS domains that provides name resolution by using Microsoft Azure infrastructure.
* Benefits of Azure DNS:
    * **Reliability and performance**: Hosted on Azure's global network of DNS name servers, providing resiliency and high availability. Uses anycast networking, so the closest available DNS server answers each DNS query.
    * **Security**: Based on Azure Resource Manager, which provides features such as Azure role-based access control (Azure RBAC), activity logs and resource locking.
    * **Ease of Use**: Manage DNS records for your Azure services and provide DNS for your external resources as well. Integrated in the Azure portal, allows you to manage your domains and records. 
    * **Customizable virtual networks**: Supports private DNS domains.
    * **Alias records**: Use an alias record set to refer to an Azure resource, such as an Azure public IP address, an Azure Traffic Manager profile, or an Azure Content Delivery Network (CDN) endpoint. If the IP address of the underlying resource changes, the alias record set seamlessly updates itself during DNS resolution. 
* You can't use Azure DNS to buy a domain name. For an annual fee, you can buy a domain name by using App Service domains or a third-party domain name registrar. Once purchased, your domains can be hosted in Azure DNS for record management.

### Summary
In this module, you learned about some of the compute and networking services that are part of Azure. You learned about virtual machines, and the different options associated with them (such as virtual machine scale sets and virtual machine availability sets). You were also introduced to some of the networking capabilities, including virtual networking, ExpressRoute, and virtual private networks.