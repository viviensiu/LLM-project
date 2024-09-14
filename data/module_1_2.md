## Cloud Concepts: Describe the benefits of using Cloud Services

### Benefits of high availability and scalability in the cloud
* When building or deploying a cloud application, two of the biggest considerations are:
    - Uptime (or Availability) 
    - Ability to handle demand (or scale).

### High availability
- High availability focuses on ensuring maximum availability, regardless of disruptions or events.
- You’ll need to account for service availability guarantees for your services and applications on cloud. Azure is a highly available cloud environment with uptime guarantees depending on the service. These guarantees are part of the service-level agreements (SLAs).

- **Azure SLA** (a.k.a uptime) is measured in % for the service or application's availability. 
- The SLA agreement contains info on downtime, customer's entitlement if SLA is not met.
- It's not possible to meet 100% SLA due to:
    - no downtime available for maintenance or upgrade.
    - every components would require a backup with zero interuptions to customer.
- Hence commonly available SLAs are 99%, 99.9%, 99.95%, 99.99%.
- 99% SLA: A total of cumulated hours e.g. 1.6H downtime per week, or 7.2H per month.
- 99.9% SLA: 10 mins downtime per week, or 43.2 mins per month.
- All Azure services have their own SLA, hence it's suggested to study them and consider if these SLAs meet your business criticality expectations.

### Scalability
- Ability to adjust resources to meet demand. Scale up to meet increased traffic demands or scale down to reduce costs.
- 2 varieties: 
    - **Vertical scaling**: Increasing or decreasing the **capabilities** of resources, e.g. processing power CPU or RAM.
    - **Horizontal scaling**: Adding or Subtracting the **number** of deployed resources, e.g. VM or containers.

### Reliability (Part of Microsoft Azure Well-Architected Framework)
- Ability of a system to recover from failures and continue to function.
- The cloud has a decentralized design, which enables you to have resources deployed in regions around the world.
- You can design your applications to automatically take advantage of this increased reliability. 
- In some cases, your cloud environment itself will automatically shift to a different region for you, with no action needed on your part.

### Predictability
- 2 types: 
    - **Performance predictability**: Predicting the resources needed to deliver a positive experience for your customers, such as Autoscaling (add or reduce resources), load balancing (redirect requests to balance out heavy traffic), and high availability.
    - **Cost predictability** : Predicting or forecasting the cost of the cloud spend. You can track your real-time resource usage, monitoring resources to ensure efficient usage, and apply data analytics to find patterns and trends that help better plan resource deployments. Tools like the Total Cost of Ownership (TCO) or Pricing Calculator helps to estimate potential cloud spend.
- Both are heavily influenced by the Microsoft Azure Well-Architected Framework.

### Governance and Compliance in the cloud
- Setting templates help ensure that all your deployed resources meet corporate standards and government regulatory requirements.
- You can update all your deployed resources to new standards as standards change.
- Auditing: flag any resource that’s out of compliance with your corporate standards and provides mitigation strategies.
- Software patches and updates.

### Security in the cloud
- IaaS (Maximum security): You're in control of manage the operating systems and installed software, including patches and maintenance.
- PaaS: Patches and maintenance taken care of automatically.
- Because the cloud is intended as an over-the-internet delivery of IT resources, cloud providers are typically well suited to handle things like distributed denial of service (DDoS) attacks, making your network more robust and secure.

### Manageability in the cloud
- **Management of the cloud** speaks to managing your cloud resources. 
    - Automatically scale resource deployment based on need.
    - Deploy resources based on a preconfigured template, removing the need for manual configuration.
    - Monitor the health of resources and automatically replace failing resources.
    - Receive automatic alerts based on configured metrics, so you’re aware of performance in real time.

- **Management in the cloud** means how you’re able to manage your cloud environment and resources. 4 ways:
    - Through a web portal.
    - Using a command line interface.
    - Using APIs.
    - Using PowerShell.

### Summary
In this module, you learned about some of the benefits of operating in the cloud. You learned about high availability and reliability, and how those work to keep your applications running. You also learned about how the cloud can provide a more secure environment. Finally, you learned that the cloud provides a highly manageable environment for your resources.

