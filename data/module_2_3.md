## Microsoft Azure Fundamentals: Describe Azure storage accounts

### Azure storage accounts
* Provides a unique namespace for your Azure Storage data that's accessible from anywhere in the world over HTTP or HTTPS. Data in this account is secure, highly available, durable, and massively scalable.
* To create a storage account, you need to pick:
    * Storage account type: This determines your services and redundancy options, and impact your use cases.
    * Unique name between 3-24 chars, lowercase and numbers only.
* Types of storage accounts:
    * Standard general-purpose v2. Supported services: Blob Storage (including Data Lake Storage), Queue Storage, Table Storage, and Azure Files. Redundancy Options: LRS, GRS, RA-GRS, ZRS, GZRS, RA-GZRS. Usage: Standard storage account type for blobs, file shares, queues, and tables. Recommended for most scenarios using Azure Storage. If you want support for network file system (NFS) in Azure Files, use the premium file shares account type.
    * Premium block blobs. Supported services: Blob Storage (including Data Lake Storage). Redundancy Options: LRS, ZRS. Usage: Premium storage account type for block blobs and append blobs. Recommended for scenarios with high transaction rates or that use smaller objects or require consistently low storage latency.
    * Premium file shares. Supported services: Azure Files. Redundancy Options:	LRS, ZRS. Usage: Premium storage account type for file shares only. Recommended for enterprise or high-performance scale applications. Use this account type if you want a storage account that supports both Server Message Block (SMB) and NFS file shares.
    * Premium page blobs. Supported services: Page blobs only. Redundancy Options: LRS. Usage: Premium storage account type for page blobs only.

* Redundancy options:
    * Locally redundant storage (LRS).
    * Geo-redundant storage (GRS).
    * Read-access geo-redundant storage (RA-GRS).
    * Zone-redundant storage (ZRS).
    * Geo-zone-redundant storage (GZRS).
    * Read-access geo-zone-redundant storage (RA-GZRS).

* **Storage account endpoints**: The combination of the storage account name and the Azure Storage service endpoint forms the endpoints for your storage account.
* The following shows the endpoint format for Azure Storage services:
    * Blob Storage: ```https://<storage-account-name>.blob.core.windows.net```.
    * Data Lake Storage Gen2: ```https://<storage-account-name>.dfs.core.windows.net```.
    * Azure Files: ```https://<storage-account-name>.file.core.windows.net```.
    * Queue Storage: ```https://<storage-account-name>.queue.core.windows.net```.
    * Table Storage: ```https://<storage-account-name>.table.core.windows.net```.

### Azure storage redundancy
* Redundancy ensures that your storage account meets its availability and durability targets even in the face of failures.
* Factors to consider when choosing a storage redundancy option:
    * How your data is replicated in the primary region.
    * Whether your data is replicated to a second region that is geographically distant to the primary region, to protect against regional disasters.
    * Whether your application requires read access to the replicated data in the secondary region if the primary region becomes unavailable.

* **Redundancy in the primary region**: Data is always replicated three times in the primary region.
* 2 options on data replication:
    * **Locally Redundant Storage (LRS)**: Lowest cost option, replicate data 3 times in a data center, protects your data against server rack and drive failures, but all data may be lost if disaster struck the data center.
    ![alt text](https://github.com/viviensiu/Azure/blob/main/images/locally-redundant-storage.png)
    * **Zone-Redundant Storage (ZRS)**: Replicates data synchronously across 3 Availability Zones in the primary region. If one zone is down, you still have both read and write access to data, no remounting required, and Azure will handle the network updates to point to direct application to the other zones. However, you will need to wait for Azure to complete network updates before you could access the data again. ZRS is recommended for restricting replication of data within a country or region to meet data governance requirements.
    ![alt text](https://github.com/viviensiu/Azure/blob/main/images/zone-redundant-storage.png)

* **Redundancy in a secondary region**: The paired secondary region is based on Azure Region Pairs, and can't be changed.
* By default, data in the secondary region isn't available for read or write access unless there's a failover to the secondary region.
* **Because data is replicated to the secondary region asynchronously, a failure that affects the primary region may result in data loss if the primary region can't be recovered. The interval between the most recent writes to the primary region and the last write to the secondary region is known as the recovery point objective (RPO). The RPO indicates the point in time to which data can be recovered. Azure Storage typically has an RPO of less than 15 minutes, although there's currently no SLA on how long it takes to replicate data to the secondary region.**
* 2 options:
    * **Geo-redundant storage (GRS)**: Copies your data synchronously 3 times within one location in primary region using LRS. It then copies your data asynchronously to a single location in the secondary region (the region pair) using LRS.
    ![alt text](https://github.com/viviensiu/Azure/blob/main/images/geo-redundant-storage.png)
    * **Geo-zone-redundant storage (GZRS)**: Combines the high availability provided by redundancy across availability zones with protection from regional outages provided by geo-replication. Data in a GZRS storage account is copied across 3 Availability Zones in the primary region (similar to ZRS) and replicated to a secondary geographic region, using LRS, for protection from regional disasters. 
    ![alt text](https://github.com/viviensiu/Azure/blob/main/images/geo-zone-redundant-storage.png)

* **Read access to data in the secondary region**:
    * Geo-redundant storage (with GRS or GZRS) replicates your data to another physical location in the secondary region to protect against regional outages. However, that data is available to be read only if the customer or Microsoft initiates a failover from the primary to secondary region. 
    * However, if you enable read access to the secondary region, your data is always available, even when the primary region is running optimally. For read access to the secondary region, enable read-access geo-redundant storage (RA-GRS) or read-access geo-zone-redundant storage (RA-GZRS).

### Azure storage services
* Benefits: 
    * Durable and highly available due to redundancy.
    * Secure as data written to an Azure storage account is encrypted by the service. Provides fine-grained control on data access authority.
    * Scalable. 
    * Managed. Azure handles hardware maintenance, updates, and critical issues for you.
    * Accessible from anywhere in the world over HTTP or HTTPS. Microsoft provides client libraries for Azure Storage in a variety of languages. Supports scripting in Azure PowerShell or Azure CLI. Azure portal and Azure Storage Explorer offer easy visual solutions for working with your data.
### Azure Blobs
* A massively scalable object store for unstructured data (text and binary). 
* Also includes support for big data analytics through Data Lake Storage Gen2. * One advantage of blob storage over disk storage is that it doesn't require developers to think about or manage disks.
* Different access tiers for blob storage to manage costs:
    * Hot access tier: Optimized for storing data that is accessed frequently (for example, images for your website). Set at account/blob level.
    * Cool access tier: Optimized for data that is infrequently accessed and stored for at least 30 days (for example, invoices for your customers). Set at account/blob level.
    * Cold access tier: Optimized for storing data that is infrequently accessed and stored for at least 90 days. Set at blob level.
    * Archive access tier: Appropriate for data that is rarely accessed and stored for at least 180 days, with flexible latency requirements (for example, long-term backups). Set at blob level.
* Access costs increase from Hot access tier to Archive access tier, while storage costs decrease from Hot access tier to Archive access tier.

### Azure Files
* Managed file shares accessible via the industry standard Server Message Block (SMB) or Network File System (NFS) protocols for cloud or on-premises deployments.
* SMB Azure file shares: Accessible from Windows, Linux, and macOS clients. Can be cached on Windows Servers with Azure File Sync.
* NFS Azure Files shares: Accessible from Linux or macOS clients.
* Benefits:
    * Shared access.
    * Fully managed: Without the need to manage hardware or an OS. 
    * Scripting and tooling: PowerShell cmdlets and Azure CLI can be used to create, mount, and manage Azure file shares. Also can use Azure portal and Azure Storage Explorer.
    * Resiliency: Always available.
    * Familiar programmability: Applications running in Azure can access data in the share via file system I/O APIs. Developers can therefore use their existing code and skills to migrate existing applications. In addition to System IO APIs, you can use Azure Storage Client Libraries or the Azure Storage REST API.

### Azure Queues 
* A messaging store for reliable messaging between application components.
* Used to create a backlog of work to process asynchronously.
* Can be combined with Azure Functions to take an action when a message is received. 

### Azure Disks 
* Block-level storage volumes for Azure VMs.
* Conceptually, they’re the same as a physical disk, but they’re virtualized.

### Azure Tables
* NoSQL table option for structured, non-relational data.

### Azure data migration options
* 2 options:   
    * Real-time migration using Azure Migrate.
    * Asynchronous migration using Azure Data Box.

### Azure Migrate
* Helps manage the assessment and migration of on-premises datacenter to Azure cloud. Provides the following:
    * Unified migration platform: A single portal to start, run, and track your migration to Azure.
    * Integrated tools including tools from independent software vendor (ISV).
    * Assessment and migration: Using the Azure Migrate hub.
* Integrated tools: 
    * **"Azure Migrate: Discovery and assessment"**: Discover and assess on-premises servers running on VMware, Hyper-V, and physical servers in preparation for migration to Azure.
    * **"Azure Migrate: Server Migration"**: Migrate VMware VMs, Hyper-V VMs, physical servers, other virtualized servers, and public cloud VMs to Azure.
    * **Data Migration Assistant**: Stand-alone tool to assess SQL Servers. It helps pinpoint potential problems blocking migration, identifies unsupported features, new features that can benefit you after migration, and the right path for database migration.
    * **Azure Database Migration Service**: Migrate on-premises databases to Azure VMs running SQL Server, Azure SQL Database, or SQL Managed Instances.
    * **Azure App Service migration assistant**: Standalone tool to assess on-premises websites for migration to Azure App Service. Use Migration Assistant to migrate .NET and PHP web apps to Azure.
    * **Azure Data Box**: Move large amounts of offline data to Azure.

### Azure Data Box
* Physical migration service that helps transfer large amounts of data in a quick, inexpensive, and reliable way.
* To import or export data from Azure. If to import data into Azure, Microsoft automatically uploads the data once they receive it.
* Maximum usable storage capacity of 80 terabytes.
* Use cases for importing data into Azure:
    *Onetime migration.
    * Moving a media library from offline tapes into Azure to create an online media library.
    * Migrating your VM farm, SQL server, and applications to Azure.
    * Moving historical data to Azure for in-depth analysis and reporting using HDInsight.
    * Initial bulk transfer.
    * Periodic uploads.
* Use cases for exporting data from Azure:
    * Disaster recovery.
    * Security requirements.
    * Migrate back to on-premises or to another cloud service provider.
* Once the data from your import order is uploaded to Azure, the disks on the device are wiped clean in accordance with NIST 800-88r1 standards. For an export order, the disks are erased once the device reaches the Azure datacenter

### Azure file movement options
* Helps you move or interact with individual files or small file groups.
* **AzCopy**: Command-line utility to upload, download, copy blobs or files between storage account, synchronize files (uni-directional only).
* **Azure Storage Explorer**: Standalone app with GUI to manage files and blobs in your Azure Storage Account, uses AzCopy on the backend.
* **Azure File Sync**: Tool that lets you centralize your file shares in Azure Files.  Once you install Azure File Sync on your local Windows server, it will automatically stay bi-directionally synced with your files in Azure. With Azure File Sync, you can:
    * Use any protocol that's available on Windows Server to access your data locally, including SMB, NFS, and FTPS.
    * Have as many caches as you need across the world.
    * Replace a failed local server by installing Azure File Sync on a new server in the same datacenter.
    * Configure cloud tiering so the most frequently accessed files are replicated locally, while infrequently accessed files are kept in the cloud until requested. 

### Summary
In this module, you learned about the Azure storage services. You learned about the Azure Storage Account and how they relate to different storage services. You were introduced to storage blobs and redundancy options, and ways to migrate and move your data both into and within Azure.