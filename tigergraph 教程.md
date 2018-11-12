---
title: "Habits"
output:
  pdf_document:
    toc: true
    toc_depth: 2
toc:
  depth_from: 1
  depth_to: 6
  ordered: false
html:
  embed_local_images: false
  embed_svg: true
  offline: false
  toc: true
puppeteer:
  landscape: true
  format: "A4"
print_background: false
export_on_save:
  html: true
  phantomjs: true
  // or
  phantomjs: "pdf"
  phantomjs: "jpeg"
  phantomjs: "png"
  phantomjs: ["pdf", "png", ...]
ebook:
  title: Alice's Adventures in Wonderland
  cover: cover0.jpg
---
[TOC]
## 开始TigerGraph
###  下载TigerGraph
DOWNLOAD the TigerGraph platform: www.tigergraph.com/download
### 安装tigergraph
```shell
tar xzf < your_tigergraph_package >.tar.gz
cd tigergraph*/
./install.sh
```
## TigerGraph 平台说明
### 架构说明
![enter image description here](https://doc.tigergraph.com/attachments/559972540/559874168.png?height=400)
### Tigergraph 权限架构说明
![用户架构](https://doc.tigergraph.com/attachments/559972540/560005220.png?width=600)
### 词汇表

<table class="wrapped relative-table confluenceTable" style="width: 100.0%;">
        <colgroup>
         <col style="width: 12.2807%;">
         <col style="width: 87.7193%;">
        </colgroup>
        <thead>
         <tr>
          <th class="confluenceTh">
           <div class="tablesorter-header-inner">
            Name
           </div>
          </th>
          <th class="confluenceTh">
           <div class="tablesorter-header-inner">
            Refers to
           </div>
          </th>
         </tr>
        </thead>
        <tbody>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            DDL
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           <p>
            Data Definition Language - a generic term for a set of commands used to define a database schema. The GSQL Language includes DDL commands. In GraphStudio, the Design Schema function.
           </p>
          </td>
         </tr>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            Dictionary (DICT)
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           The shared storage space for storing metadata about the graph store's configuration and state, including the catalog (graph schema, loading jobs, and queries).
          </td>
         </tr>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            DML
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           Data Manipulation Language - a generic term for a set of commands used to add, modify, and delete data from a database. Query commands are often considered a part of DML, even a pure query statement does not manipulate (change) the data. The GSQL Language includes full DML capability for query, add (insert), delete, and modify (update) commands.
          </td>
         </tr>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            gadmin
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           The system utility for configuring and managing the TigerGraph&nbsp;System. Analogous to mysqladmin.
          </td>
         </tr>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            gbar
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           Graph Backup
           and Restore. TigerGraph's utility program for backing up and restoring system data.
          </td>
         </tr>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            GPE
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           Graph Processing Engine. The server component which accepts requests from the REST++ server for querying and updating the graph store and which returns data.
          </td>
         </tr>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            Graph Store
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           The component which logically and physically stores the graph data and provides access to the data in a fast and memory-efficient way. We use the term graph store to distinguish it from conventional graph databases.
          </td>
         </tr>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            GraphStudio UI
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           The browser-based User Interface that enables the user to interact with the TigerGraph&nbsp;system in a visual and intuitive way, as an alternative to the GSQL Shell. The GraphStudio UI includes the following components: Schema Designer, Data Mapper, Data Loader, Graph Explorer, and Query Editor.
          </td>
         </tr>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            GSE
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           Graph Storage Engine. The processing component which manages the Graph Store.
          </td>
         </tr>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            GSQL
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           <p>
            The user program which interprets and executes graph processing operations, including (a) schema definition, (b) data loading, and (c) data updates, and (d) data queries.
           </p>
          </td>
         </tr>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            GSQL Language
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           The language used to instruct and communicate with the GSQL program.
          </td>
         </tr>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            GSQL Shell
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           The&nbsp;interactive command shell which may be used when running the GSQL program.
          </td>
         </tr>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            HA
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           High Availability - a generic term describing a computer system which has been architected to a higher level of operational performance (e.g., throughput and uptime) than would be expected from a traditional single server node.
          </td>
         </tr>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            IDS
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           ID Service. A subcomponent of the GSE which translates between user (external) IDs for data objects and graph store (internal) IDs.
          </td>
         </tr>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            IUM
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           Installation, Upgrade, and Maintenance (generic term). These functions are handled by gadmin.
          </td>
         </tr>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            Kafka
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           A free open-source "high-throughput distributed messaging system" from the Apache Software Foundation. Our distributed system architecture is based on message passing/queuing. Kafka is automatically included during TigerGraph&nbsp;system installation as one implementation of messaging passing.
           <a class="external-link" href="https://kafka.apache.org/">
            https://kafka.apache.org/
           </a>
          </td>
         </tr>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            MultiGraph
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           A graph architecture and feature set which enables one global graph to be viewed as multiple logical subgraphs, each with its own set of user privileges. The subgraphs can overlap, meaning each subraph can support both shared and private data.
          </td>
         </tr>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            Native Parallel Graph
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           An architecture and technology which provides for inherently highly-parallel and highly-scalable graph data storage and analytics. The use of vertex-level data+compute functionality is a key component of Native Parallel Graph design.
          </td>
         </tr>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            Nginx
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           A
           <span style="color: rgb(64,64,64);">
            <span>
            </span>
            free, open-source, high-performance HTTP server and reverse proxy. Nginx is automatically included during TigerGraph system installation.
            <a class="external-link" href="https://nginx.org/en/">
             https://nginx.org/en/
            </a>
           </span>
          </td>
         </tr>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            REST++
           </strong>
           or
           <br>
           <strong>
            RESTPP
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           <p>
            A server component which accepts RESTful requests from clients, validates the requests, invokes the GPE, and sends responses back to the client.&nbsp;Additionally,
            <span>
             REST++ provides a zero-coding interface for users to define RESTful endpoints.
            </span>
            <span style="line-height: 1.42857;">
             REST++ offers easy-to-use APIs for customizing the logic of handling requests and processing responses.
            </span>
           </p>
          </td>
         </tr>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            Single Sign-On (SSO)
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           A
           <span style="color: rgb(108,108,108);">
            user
            <span>
            </span>
           </span>
           authentication
           <span style="color: rgb(108,108,108);">
            <span>
            </span>
            service that permits a user to use one set of
            <span>
            </span>
           </span>
           login
           <span style="color: rgb(108,108,108);">
            <span>
            </span>
            credentials to access multiple applications.
           </span>
          </td>
         </tr>
         <tr>
          <td class="confluenceTd">
           <strong>
            TigerGraph
            <br>
            Platform
           </strong>
          </td>
          <td class="confluenceTd">
           The TigerGraph&nbsp;real-time graph data analytics software system. The TigerGraph&nbsp;Platform offers complete functionality for creating and managing a graph database and for performing data queries and analyses. The platform includes the
           Graph Store and GSE
           , GPE, REST++, GSQL, GraphStudio, plus some third-party components, such as Apache Kafka and Zookeeper.
          </td>
         </tr>
         <tr>
          <td class="confluenceTd">
           <strong>
            TigerGraph
           </strong>
           <br>
           <strong>
            System
           </strong>
          </td>
          <td class="confluenceTd">
           <p>
            <span style="line-height: 1.42857;">
             The TigerGraph&nbsp;platform and its languages. Based on context, the term may also include additional optional TigerGraph&nbsp;components which have been installed.
            </span>
           </p>
          </td>
         </tr>
         <tr>
          <td class="confluenceTd" colspan="1">
           <strong>
            Zookeeper
           </strong>
          </td>
          <td class="confluenceTd" colspan="1">
           A free open-source program from the Apache Software Foundation, providing "a
           <span style="color: rgb(0,0,0);">
            centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services." Used for running the TigerGraph&nbsp;system on a cluster or other distributed system. Zookeeper is automatically included during TigerGraph&nbsp;system installation.
            <a class="external-link" href="https://zookeeper.apache.org/">
             https://zookeeper.apache.org/
            </a>
           </span>
          </td>
         </tr>
        </tbody>
       </table>
## TigerGraph Demo Example
### TigerGraph 查询流程图
![流程图](https://doc.tigergraph.com/attachments/560562303/559906981.png)
### TigerGraph 创建点和线
```SQL
CREATE VERTEX User (PRIMARY_ID id string)
CREATE DIRECTED EDGE Liked (FROM User, TO User) WITH REVERSE_EDGE = "Liked_By"
```
### 通过JOB加载数据
**cf_data.csv**
```csv
id2,id1
id2,id3
id3,id1
id3,id4
id5,id1
id5,id2
id5,id4
```
**cf_load.gsql**
```SQL
# define the loading job
USE GRAPH gsql_demo # added for v1.2
CREATE LOADING JOB load_cf FOR GRAPH gsql_demo {
  DEFINE FILENAME f;
  LOAD f
    TO VERTEX User VALUES ($0),
    TO VERTEX User VALUES ($1),
    TO EDGE Liked VALUES ($0, $1);
}

# load the data
RUN LOADING JOB load_cf USING f="../cf/data/cf_data.csv"
```
