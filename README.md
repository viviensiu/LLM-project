# AZ-900 Study Buddy

## Table of contents
* [Problem Statement](https://github.com/viviensiu/LLM-project/blob/main/README.md#problem-statement)
* [Dataset](https://github.com/viviensiu/LLM-project/blob/main/README.md#dataset)
* [Tech Stack](https://github.com/viviensiu/LLM-project/blob/main/README.md#tech-stack)
* [Good-to-have](https://github.com/viviensiu/LLM-project/blob/main/README.md#good-to-have)
* [Methodology](https://github.com/viviensiu/LLM-project/blob/main/README.md#methodology)

## Problem Statement
<p align="center">
    <img src="https://github.com/viviensiu/LLM-project/blob/main/image/problem.jpg" width=200>
</p>
Studying and preparing for course exams can be overwhelming and time-consuming, especially when there are too many materials. Often times, one needs to look up information on a specific topic, but having trouble to know where to find it. 

Hence, a RAG application using course materials as a knowledge base could help to optimise the time and effort spent in studies and preparation for exams.

As I'm currently studying for the Azure Foundation certification AZ-900 exam, my RAG application **AZ-900 Study Buddy** aims to address these common issues above and serve as an example on how RAG could be applied to educational use cases in general.

## Dataset
* All data used/generated for this project are available in [data folder](https://github.com/viviensiu/LLM-project/tree/main/data).
* Raw data: My AZ900 course notes, see `module_*.md` files.
* [readme_notes_with_ids.json](https://github.com/viviensiu/LLM-project/blob/main/data/readme_notes_with_ids.json): Raw data that are loaded and chunked into JSON format.
* [az900_notes_with_vectors.pkl](https://github.com/viviensiu/LLM-project/blob/main/data/az900_notes_with_vectors.pkl): The RAG knowledge base source which is a structured data with vector embeddings.
* [ground-truth-data.pkl](https://github.com/viviensiu/LLM-project/blob/main/data/ground-truth-data.pkl): Ground truth data with questions for retrieval and RAG evaluation stage.
* [RAG_evaluation.pkl](https://github.com/viviensiu/LLM-project/blob/main/data/RAG_evaluation.pkl): LLM generated responses, cosine similarity and latency data during RAG evaluation stage.
* [results_backup.json](https://github.com/viviensiu/LLM-project/blob/main/data/results_backup.json): A backup of JSON format questions generated during ground truth generation stage (to skip question regeneration if any error occurs during parsing).

## Tech Stack
* Python 3.12.
* Docker.
* Elasticsearch for knowledge base retrieval.
* OpenAI or Ollama for LLM.

## Good-to-have
* Basic knowledge of these Docker commands for troubleshooting: `docker ps`, `docker ps -a`, `docker start`, `docker compose up`, `docker compose down`.

## Methodology
There are 4 main steps, the first 2 steps:
* Ingestion: load, chunk and embed.
* Evaluation: retrieval and RAG.
<p align="center">
<img src="https://github.com/viviensiu/LLM-project/blob/main/image/methodology.png" width=800>
</p>
Once the best retrieval method and RAG is determined, the app. **AZ900 Study Buddy** is then built in these 2 steps:
* Interface: streamlit application and RAG class.
* Containerization: dockerize application, knowledge base and LLM using docker compose.
<p align="center">
<img src="https://github.com/viviensiu/LLM-project/blob/main/image/az900_flow.png" width=800>
</p>

## Env setup (one-time)
* ```conda create -n llm-zoomcamp-env python```
* ```conda activate llm-zoomcamp-env```
* ```conda install pip```
* ```pip install pipenv```
* ```pipenv install tqdm notebook==7.1.2 openai elasticsearch pandas jupyter sentence_transformers==2.7.0 python-dotenv seaborn streamlit```
* Docker is installed at your local desktop, you could download it at [Download Docker Desktop](https://www.docker.com/products/docker-desktop/).

## Activating virtual env for this project
* ```conda activate llm-zoomcamp-env```
* ```pipenv shell```

## Experimentation
* **Purpose**:
* **Setup**:
* To check if elasticsearch container is running, go to [http://localhost:9200/](http://localhost:9200/).
* If not, either start up your existing elasticsearch container using `docker start elasticsearch` or start a new elasticsearch container with the following command: 
```bash
docker run -it \
    --name elasticsearch \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.4.3
```

## Instructions to setup and run this app locally
* Create a new folder on your Desktop: `AZ900_study_buddy`. You could of course use another folder name and location, but by following this guideline it helps you to remember where you have saved it to!
* Download this zip file to the `AZ900_study_buddy` on your Desktop.
* Unzip the downloaded zip file.
* Rename `.env_template` to `.env`
* Make sure Docker service is up and running.
* There are 2 LLM options to be used in the application: GPT-4o-mini and Ollama Phi3. 
    * If you go for the GPT-4o-mini option, you will be prompted to select GPT-4o-mini and enter your OpenAI API key at the application screen. 
    * **(Optional)To use Ollama Phi3**: You need to have a **running ollama container** in Docker (check if ollama is running using `docker ps`. If not running, check if you have a stopped ollama container using `docker ps -a`, if one exists, restart container using `docker start ollama`). Once ollama container is running, check if the ollama container has a Phi3 model already by doing the following:
    ```bash
    docker exec -it ollama bash
    ollama list
    ```
    * If you can see a **phi3** model then you could use Ollama Phi3 to test the app.
    ![alt text](https://github.com/viviensiu/LLM-project/blob/main/image/ollama_list_example.png)
    * Otherwise execute `ollama pull phi3`.
    ![alt text](https://github.com/viviensiu/LLM-project/blob/main/image/ollama_pull_phi3_example.png)
    * **(Optional) For those without any existing Ollama container, please execute first** the following Docker commands in command prompt:
```bash
docker run -it \
    --rm \
    -v ollama:/root/.ollama \
    -p 11434:11434 \
    --name ollama \
    ollama/ollama
```
    * if the above is successful, you should see an ollama container when you execute the command ```docker ps```.
    * After that, pull Phi3 model into the ollama container by executing:
```bash
docker exec -it ollama bash
ollama pull phi3
```
* Open up a command prompt session or in your VSCode terminal, execute the following:
    * Navigate to the folder which contains all unzipped files for this application.
    * Run `docker compose up` or `docker compose up -d`(detached mode if you don't want your command line session to be "locked" by a running container session).
    * Run `docker ps` to cross check that containers are up, you should be able to see containers with names `az900_study_buddy_app` and `elasticsearch` up and running.
    * (Optional) To double check that indices are created in elasticsearch, do
    ```bash
    curl -X GET "http://localhost:9200/_cat/indices?v"
    ```
    or copy-paste [http://localhost:9200/_cat/indices?v](http://localhost:9200/_cat/indices?v) in browser. If the knowledge base is indexed you should see `az900_course_notes` under "index".
* Open a browser and copy-paste this link [http://localhost:8501/](http://localhost:8501/) into the browser. If the setup is successful, you should now see the following screen: 


## Evaluation Criteria

* Problem description
    * This is an Azure foundation (AZ-900) exam study buddy chatbot, which aims to help fellow students who are taking this exam to retrieve relevant notes during their studies.
    * A quick way to look up
* RAG flow
    * 0 points: No knowledge base or LLM is used
    * 1 point: No knowledge base is used, and the LLM is queried directly
    * **2 points: Both a knowledge base and an LLM are used in the RAG flow** 
* Retrieval evaluation
    * 0 points: No evaluation of retrieval is provided
    * 1 point: Only one retrieval approach is evaluated
    * **2 points: Multiple retrieval approaches are evaluated, and the best one is used**
* RAG evaluation
    * 0 points: No evaluation of RAG is provided
    * 1 point: Only one RAG approach (e.g., one prompt) is evaluated
    * **2 points: Multiple RAG approaches are evaluated, and the best one is used**
* Interface
   * 0 points: No way to interact with the application at all
   * 1 point: Command line interface, a script, or a Jupyter notebook
   * **2 points: UI (e.g., Streamlit), web application (e.g., Django), or an API (e.g., built with FastAPI)** 
* Ingestion pipeline
   * 0 points: No ingestion
   * 1 point: Semi-automated ingestion of the dataset into the knowledge base, e.g., with a Jupyter notebook
   * **2 points: Automated ingestion with a Python script or a special tool (e.g., Mage, dlt, Airflow, Prefect)**
* Monitoring
   * 0 points: No monitoring
   * 1 point: User feedback is collected OR there's a monitoring dashboard
   * 2 points: User feedback is collected and there's a dashboard with at least 5 charts
* Containerization
    * 0 points: No containerization
    * 1 point: Dockerfile is provided for the main application OR there's a docker-compose for the dependencies only
    * 2 points: Everything is in docker-compose
* Reproducibility
    * 0 points: No instructions on how to run the code, the data is missing, or it's unclear how to access it
    * 1 point: Some instructions are provided but are incomplete, OR instructions are clear and complete, the code works, but the data is missing
    * 2 points: Instructions are clear, the dataset is accessible, it's easy to run the code, and it works. The versions for all dependencies are specified.
* Best practices
    * **[ ] Hybrid search: combining both text and vector search (at least evaluating it) (1 point)**
    * **[ ] Document re-ranking (1 point)**
    * [ ] User query rewriting (1 point)
* Bonus points (not covered in the course)
    * [ ] Deployment to the cloud (2 points)
