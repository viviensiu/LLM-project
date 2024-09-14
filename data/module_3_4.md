## Microsoft Azure Fundamentals: Describe monitoring tools in Azure

### Azure Advisor
* It evaluates your Azure resources and makes recommendations available via the Azure portal and the API to help save time in optimising your cloud resources. The recommendation service includes suggested actions you can take right away, postpone, or dismiss. You can set up notifications to alert you to new recommendations.
* The recommendations are divided into 5 categories:
    * **Reliability**: Ensure and improve the continuity of your business-critical applications.
    * **Security**: Detect threats and vulnerabilities that might lead to security breaches.
    * **Performance**: mprove the speed of your applications.
    * **Operational Excellence**: Help you achieve process and workflow efficiency, resource manageability, and deployment best practices.
    * **Cost**: Optimize and reduce your overall Azure spending.
* Azure Advisor dashboard:
![alt text](https://github.com/viviensiu/Azure/blob/main/images/azure-advisor-dashboard.png)

### Azure Service Health 
* Helps you keep track of Azure resource, both your specifically deployed resources and the overall status of Azure. Combines 3 different Azure services:
    * **Azure Status**: Informs you of service outages in Azure on the Azure Status page. The page is a global view of the health of all Azure services across all Azure regions. It’s a good reference for incidents with widespread impact.
    * **Service Health**: A narrower view of Azure services and regions. It focuses on the Azure **services and regions you're using**. This is the best place to look for service-impacting communications about outages, planned maintenance activities, and other health advisories because the authenticated Service Health experience knows which services and resources you currently use. You can even set up Service Health alerts to notify you when service issues, planned maintenance, or other changes may affect the Azure services and regions you use.
    * **Resource Health**: Tailored view that provides information about the health of **your individual cloud resources**, such as a specific VM instance. Using Azure Monitor, you can also configure alerts to notify you of availability changes to your cloud resources.
* Historical alerts are stored and accessible for later review. Something you initially thought was a simple anomaly that turned into a trend, can readily be reviewed and investigated thanks to the historical alerts.
*  If a workload you’re running is impacted by an event, Azure Service Health provides links to support.

### Azure Monitor
* A platform for collecting data on your resources, analyzing that data, visualizing the information, and even acting on the results. 
* It can monitor Azure resources, your on-premises resources, and even multi-cloud resources like virtual machines hosted with a different cloud provider.
![alt text](https://github.com/viviensiu/Azure/blob/main/images/azure-monitor-overview.svg)
* A breakdown of the Azure Monitor dashboard:
    * Left panel: A list of the sources of logging and metric data that can be collected at every layer in your application architecture, from application to operating system and network.
    * Center panel: Logging and metric data are stored in central repositories.
    * Right panel: The data is used in several ways. You can view real-time and historical performance across each layer of your architecture or aggregated and detailed information. The data is displayed at different levels for different audiences. You can view high-level reports on the Azure Monitor Dashboard or create custom views by using Power BI and Kusto queries. Additionally, you can use the data to help you react to critical events in real time, through alerts delivered to teams via SMS, email, and so on. Or you can use thresholds to trigger autoscaling functionality to scale to meet the demand.

### Azure Log Analytics
* Azure portal tool to write and run log queries on the data gathered by Azure Monitor. 
* Supports both simple, complex queries, and data analysis. You can write a simple query that returns a set of records and then use features of Log Analytics to sort, filter, and analyze the records. You can write an advanced query to perform statistical analysis and visualize the results in a chart to identify a particular trend. 
* Whether you work with the results of your queries interactively or use them with other Azure Monitor features such as log query alerts or workbooks, Log Analytics is the tool that you're going to use to write and test those queries.

### Azure Monitor Alerts 
* An automated way to stay informed when Azure Monitor detects a threshold being crossed. 
* Alerts can be set up to monitor the logs and trigger on certain log events, or they can be set to monitor metrics and trigger when certain metrics are crossed. Alert rules based on metrics provide near real time alerts based on numeric values. Rules based on logs allow for complex logic across data from multiple sources.
* Azure Monitor Alerts use action groups to configure who to notify and what action to take. An action group is a collection of notification and action preferences that you associate with one or multiple alerts. **Azure Monitor, Service Health, and Azure Advisor all use actions groups** to notify you when an alert has been triggered.
![alt text](https://github.com/viviensiu/Azure/blob/main/images/azure-monitor-alerts.png)

### Application Insights 
* An Azure Monitor feature that monitors your web applications running in Azure, on-premises, or in a different cloud environment.
* 2 ways to configure Application Insights: 
    * Install an SDK in your application.
    * Use the Application Insights agent which is supported in C#.NET, VB.NET, Java, JavaScript, Node.js, and Python.
* Able to monitor a broad array of information, such as:
    * Request rates, response times, and failure rates.
    * Dependency rates, response times, and failure rates, to show whether external services are slowing down performance.
    * Page views and load performance reported by users' browsers.
    * AJAX calls from web pages, including rates, response times, and failure rates
    * User and session counts.
    * Performance counters from Windows or Linux server machines, such as CPU, memory, and network usage.

### Summary
In this module, you were introduced to tools that help you monitor your environment and applications, both in Azure and in on-premises or multicloud environments.