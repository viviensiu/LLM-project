# AZ-900 Study Buddy

## Table of contents
* [Problem Statement](https://github.com/viviensiu/LLM-project/blob/main/README.md#problem-statement)
* [Dataset](https://github.com/viviensiu/LLM-project/blob/main/README.md#dataset)
* [Tech Stack](https://github.com/viviensiu/LLM-project/blob/main/README.md#tech-stack)
* [Must-have](https://github.com/viviensiu/LLM-project/blob/main/README.md#must-have)
* [Good-to-have](https://github.com/viviensiu/LLM-project/blob/main/README.md#good-to-have)
* [Methodology](https://github.com/viviensiu/LLM-project/blob/main/README.md#methodology)
* [Environment setup](https://github.com/viviensiu/LLM-project/blob/main/README.md#environment-setup)
    * [.env_template](https://github.com/viviensiu/LLM-project/blob/main/.env_template)
    * [Elastic Search](https://github.com/viviensiu/LLM-project/blob/main/README.md#elastic-search)
* [Running the application using docker compose](https://github.com/viviensiu/LLM-project/blob/main/README.md#running-the-application-using-docker-compose)
    * [Pick your LLM](https://github.com/viviensiu/LLM-project/blob/main/README.md#pick-your-llm)
    * [Start up application](https://github.com/viviensiu/LLM-project/blob/main/README.md#start-up-application)
    * [How to use the application](https://github.com/viviensiu/LLM-project?tab=readme-ov-file#how-to-use-the-application)
    * [Stopping the application](https://github.com/viviensiu/LLM-project?tab=readme-ov-file#stopping-the-application)
* [Evaluation Criteria](https://github.com/viviensiu/LLM-project/blob/main/README.md#evaluation-criteria)
* [Future works](https://github.com/viviensiu/LLM-project/blob/main/README.md#future-works)
* [Credits](https://github.com/viviensiu/LLM-project/blob/main/README.md#credits)
* [Contact info for peers](https://github.com/viviensiu/LLM-project/blob/main/README.md#contact-info-for-peers)

## Problem Statement
<p align="center">
    <!--img src="https://github.com/viviensiu/LLM-project/blob/main/image/problem.jpg" width=200 -->
   <img src="https://imgs.xkcd.com/comics/predictive_models.png">
</p>
<p align="center">
   <em>credits: <a href="https://xkcd.com/2169/">xkcd.com</a></em>
</p>
Studying for exams can often be overwhelming and time-consuming, especially when there's a large volume of material to review. It's common to need quick access to information on specific topics but struggle to find the relevant content. To tackle this, a RAG (Retrieval-Augmented-Generation) application, built with course materials as its knowledge base, can streamline the study process by optimizing time and effort.

As I prepare for the Azure Fundamentals AZ-900 exam, I developed the **AZ-900 Study Buddy**, a RAG application designed to address these challenges. This project not only helps with exam preparation but also serves as a practical example of how RAG technology can be applied to educational use cases in general.

## Dataset
* All data for this project are available in [data folder](https://github.com/viviensiu/LLM-project/tree/main/data).
* Raw data: My AZ900 course notes, see `module_*.md` files.
* [readme_notes_with_ids.json](https://github.com/viviensiu/LLM-project/blob/main/data/readme_notes_with_ids.json): Raw data that are loaded and chunked into JSON format.
* [az900_notes_with_vectors.pkl](https://github.com/viviensiu/LLM-project/blob/main/data/az900_notes_with_vectors.pkl): The RAG knowledge base source, a structured data with vector embeddings.
* [ground-truth-data.pkl](https://github.com/viviensiu/LLM-project/blob/main/data/ground-truth-data.pkl): Ground truth data, contains questions to be used in retrieval evaluation and RAG evaluation.
* [RAG_evaluation.pkl](https://github.com/viviensiu/LLM-project/blob/main/data/RAG_evaluation.pkl): A set of LLM generated responses, cosine similarity, latency, cost and tokens usage data from RAG evaluation.
* [results_backup.json](https://github.com/viviensiu/LLM-project/blob/main/data/results_backup.json): A backup of JSON format questions generated for ground truth data (to skip question regeneration if any error occurs during parsing).

## Tech Stack
* Python 3.12.
* Docker.
* Elasticsearch for knowledge base retrieval.
* OpenAI or Ollama for LLM.

## Must-have
* Docker, since the knowledge base is indexed into elasticsearch docker container. You could download it at [Download Docker Desktop](https://www.docker.com/products/docker-desktop/).
* An OpenAI account with credits, or an Ollama docker container with Phi3 model pulled. 

## Good-to-have
* Basic knowledge of these Docker commands for troubleshooting: `docker ps`, `docker ps -a`, `docker start`, `docker compose up`, `docker compose down`.

## Methodology
There are 4 main steps, the first 2 steps:
* Ingestion: load, chunk and embed raw data into structured data with embeddings.
* Evaluation: evaluate the best retrieval and RAG methods for this use case.
<p align="center">
<img src="https://github.com/viviensiu/LLM-project/blob/main/image/methodology.png" width=700>
</p>

Once the best retrieval method and RAG is determined, the app **AZ900 Study Buddy** is then built in these 2 steps:
* Interface: streamlit application and RAG backend.
* Containerization: dockerize application, knowledge base and LLM using docker compose.
<p align="center">
<img src="https://github.com/viviensiu/LLM-project/blob/main/image/az900_flow.png" width=700>
</p>

## Environment setup 
One-time setup to reproduce any parts of this repo on your workstation. **You can skip to [Running the application using docker compose](https://github.com/viviensiu/LLM-project/blob/main/README.md#running-the-application-using-docker-compose) if you only want to run the application.**
* ```conda create -n llm-zoomcamp-env python```
* ```conda activate llm-zoomcamp-env```
* ```conda install pip```
* ```pip install pipenv```
* ```pipenv install tqdm notebook==7.1.2 openai elasticsearch pandas jupyter sentence_transformers==2.7.0 python-dotenv seaborn streamlit```
* ```pipenv shell```: This allows you to run commands such as `python xxx.py`, `streamlit run xxx.py` in the virtual environment.
* **Make sure docker service is up and running!**
* `git clone` this repo to your local workstation.
* [Prepare the .env file](https://github.com/viviensiu/LLM-project/blob/main/README.md#env-template).
* Start [elasticsearch](https://github.com/viviensiu/LLM-project/blob/main/README.md#elastic-search).

### .env template
* Refer [ChatGPT's suggestions](https://chatgpt.com/share/66e80914-4264-8001-8dae-a523469b0f9a) to view `.env*` files. Else you can't proceed with next step.
* Rename [.env_template](https://github.com/viviensiu/LLM-project/blob/main/.env_template) to `.env`. 
* **(Not applicable for running application, only for code reproduction)** Copy-paste your OpenAI API key to env. variable "OPENAI_API_KEY".

### Elastic Search
**Not applicable for running application as it's handled by docker compose**. For some code reproduction, you will need elasticsearch container to be running..
* To check if elasticsearch container is running, go to [http://localhost:9200/](http://localhost:9200/).
* If not, either start an existing elasticsearch container using `docker start elasticsearch` or a new elasticsearch container with the following command: 
```bash
docker run -it \
    --name elasticsearch \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.4.3
```

## Running the application (using docker compose)
This is for reproduction of the AZ900 Study Buddy application only (without reproducing other steps e.g. ingestion, evaluation). 
* **Make sure Docker service is up and running!**
### Pick your LLM
* There are 2 LLM options available in the application: GPT-4o-mini and Ollama Phi3. You need to decide on which one to use and to have it ready before starting the application. See diagram for setup flow:
![app setup flow](https://github.com/viviensiu/LLM-project/blob/main/image/app_setup_flow.png)
    * **GPT-4o-mini**: You will be asked to select GPT-4o-mini and input your OpenAI API key at the application screen. You can now proceed to [docker compose step](https://github.com/viviensiu/LLM-project/blob/main/README.md#start-up-application) directly.
    * **Ollama Phi3**: You need to have a **running ollama container with Phi3 model inside**.To check if you have an existing ollama container, execute `docker ps -a`. 
        * If one exists but stopped, start container with `docker start ollama`. 
        * If there's no existing Ollama container, execute the following:
```bash
docker run -it \
    --rm \
    -v ollama:/root/.ollama \
    -p 11434:11434 \
    --name ollama \
    ollama/ollama
```
* Once ollama container is running (you can see it in `docker ps`), check if the ollama container has a Phi3 model by executing:
    * `docker exec -it ollama bash`, then `ollama list`.
    * If you can see a **phi3** model then you could use Ollama Phi3 to test the app. Example:
![alt text](https://github.com/viviensiu/LLM-project/blob/main/image/ollama_list_example.png)
    * Otherwise, execute `ollama pull phi3`. Example:
![alt text](https://github.com/viviensiu/LLM-project/blob/main/image/ollama_pull_phi3_example.png)

### Start up application
* Download this zip file [az900_study_buddy.zip](https://github.com/viviensiu/LLM-project/blob/main/az900_study_buddy.zip) to your Desktop.
* Unzip the downloaded `az900_study_buddy.zip`. You should see a new folder `az900_study_buddy` on your Desktop.
* Execute the following in command prompt:
    * `cd Desktop/az900_study_buddy`.
    * Run `docker compose up`. This takes about 2-3 minutes. Once it's done you should see the following:
    ![docker compose completed](https://github.com/viviensiu/LLM-project/blob/main/image/streamlit_ready.png)
* Optional health checks:
    * Cross check containers `az900_study_buddy_app` and `elasticsearch` are up with `docker ps`. If you plan to use Ollama, you need to see `ollama` container as well, refer this guide [Pick your LLM](https://github.com/viviensiu/LLM-project/blob/main/README.md#pick-your-llm).
    * To ensure that data are indexed in elasticsearch, go to [http://localhost:9200/_cat/indices?v](http://localhost:9200/_cat/indices?v). You should see `az900_course_notes` under "index".
* To access the application, open this link [http://localhost:8501/](http://localhost:8501/) in a browser. If it is successful, you should now see the following screen: 
![app screen](https://github.com/viviensiu/LLM-project/blob/main/image/app_screen.png)
* **Note**: If you executed `docker compose up -d`(detached mode), it would only tell you the containers are started but it doesn't tell you when the Streamlit app is ready. So you might encounter 404 not found when loading [the application](http://localhost:8501/). Please try refreshing the page again after a minute or so.

### How to use the application
* You must choose an LLM model first before you could start asking questions!
* If you're using GPT-4o-mini, select "OpenAI GPT-4o-mini" in drop down list and input your API key, press submit.
* If you're using Ollama, select "Ollama Microsoft Phi3" and press submit.
* You can now start to ask questions. Here's a screenshot of the interaction using Ollama:
![sample interaction](https://github.com/viviensiu/LLM-project/blob/main/image/ollama_example.png) 

### Stopping the application
* Execute the following in command prompt:
    * `cd Desktop/az900_study_buddy`.
    * `docker compose down` 
* You could also stop your ollama container if you're done with it.

## Evaluation Criteria
For peer review: A full list of LLM zoomcamp project evaluation criteria is available [here](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/project.md#evaluation-criteria). 
* **Problem description**
    * See [Problem Statement](https://github.com/viviensiu/LLM-project/blob/main/README.md#problem-statement).
* **RAG flow**
    * Both a knowledge base and an LLM are used in the RAG flow. See [Methodology](https://github.com/viviensiu/LLM-project/blob/main/README.md#methodology).
* **Retrieval evaluation**
    * Metrics used: Hit rate and Mean Reciprocal Rank (MRR)
    * Multiple retrieval approaches are evaluated: text search, vector search, hybrid search, together with fine-tuning on the boost parameter. Refer notebook [retrieval_evaluation.ipynb](https://github.com/viviensiu/LLM-project/blob/main/experimentation/retrieval_evaluation.ipynb) for details. 
    * Hybrid search with document reranking is also evaluated. Refer notebook [hybrid_search_reranking.ipynb](https://github.com/viviensiu/LLM-project/blob/main/experimentation/hybrid_search_reranking.ipynb) for details.
    * Conclusion: Hybrid search (without document reranking) has the best retrieval performance. 
* **RAG evaluation**
    * Metrics used: Cosine similarity, latency, cost and tokens usage.
    * Models evaluated: GPT-4o-mini, GPT-3.5-turbo.
    * Multiple RAG approaches are evaluated based on metrics above. Refer notebook [RAG_evaluation.ipynb](https://github.com/viviensiu/LLM-project/blob/main/experimentation/RAG_evaluation.ipynb).
    * Conclusion: The best one, GPT-4o-mini, is used in the application.
* **Interface**
   * A Streamlit UI is used. See [app.py](https://github.com/viviensiu/LLM-project/blob/main/app/app.py)
* **Ingestion pipeline**
   * Automated ingestion within [Dockerfile](https://github.com/viviensiu/LLM-project/blob/main/Dockerfile) by auto-calling a shell script [entrypoint.sh](https://github.com/viviensiu/LLM-project/blob/main/entrypoint.sh) that runs the Python script [index_data.py](https://github.com/viviensiu/LLM-project/blob/main/app/index_data.py) to index data into elasticsearch container.
* **Monitoring**
   * Currently unavailable.
* **Containerization**
    * Everything is in docker-compose with an optional setup (if want to use Ollama Phi3 instead of GPT-4o-mini). See [Running the application (using docker compose)](https://github.com/viviensiu/LLM-project/blob/main/README.md#running-the-application-using-docker-compose).
* **Reproducibility**
    * See [Dataset](https://github.com/viviensiu/LLM-project/blob/main/README.md#dataset), [Environment setup](https://github.com/viviensiu/LLM-project/blob/main/README.md#environment-setup), [Running the application using Docker Compose](https://github.com/viviensiu/LLM-project/blob/main/README.md#running-the-application-using-docker-compose).
* **Best practices**
    * Hybrid search: refer notebook [retrieval_evaluation.ipynb](https://github.com/viviensiu/LLM-project/blob/main/experimentation/retrieval_evaluation.ipynb).
    * Document re-ranking: refer notebook [hybrid_search_reranking.ipynb](https://github.com/viviensiu/LLM-project/blob/main/experimentation/hybrid_search_reranking.ipynb).
* **Bonus points (not covered in the course)**
    * Currently unavailable in the cloud.

## Future works
* Monitoring using PostgreSQL and Grafana.
* Migrate data to MongoDB.
* Deploy app onto cloud: HuggingFace Spaces, Streamlit Cloud, AWS EC2.
* A project report to talk more about methodology, findings.

## Credits
A big thanks to Alexey Grigorev and the [DataTalks.Club](https://github.com/DataTalksClub) for the LLM Zoomcamp course, which made this project possible! :smiley:

## Contact info for peers
* For any questions regarding peer review, please reach out to me on [DataTalks.Club](https://github.com/DataTalksClub) user "Vivien S.".
* Alternatively, you can create a new issue under [Issues](https://github.com/viviensiu/LLM-project/issues).
