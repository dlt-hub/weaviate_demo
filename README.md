# Data Loading Demos

This repository contains Jupyter notebooks and more extensive projects that illustrate various methods for loading data into different destinations (e.g. Weaviate database)
using the [dlt](https://github.com/dlt-hub/dlt) library.

## Repository Contents

### Prerequisites

To run the notebooks, you will need credentials for the tools being used. They are added to the `.dlt` folder. For instance, if you're working on a Weaviate notebook, you will have to add Weaviate credentials. Refer to the notebooks to find out which credentials are needed.

### Common demos

- [schema_evolution.ipynb](schema_evolution.ipynb): shows how you can alert schema changes to slack.
- [spotlight_demo.ipynb](spotlight_demo.ipynb): shows how to get data from APIs, files, Python objects and move it into a local or remote database.
  Demo was created for a [Data Talks Club: Open-Source Spotlight](https://youtube.com/playlist?list=PL3MmuxUbc_hJ5t5nnjzC0F2zan76Dpsz0&feature=shared) project.
- [Pyladies 12.11.2024](pyladies-2024-demo): Similar to Spotlight demo, shows dlt basics, demonstrates how to get data from APIs (GitHub and PokeAPI), database, JSON, and move it into a Duckdb. 

### Weaviate demos

- [pdf_to_weaviate.ipynb](pdf_to_weaviate.ipynb): shows how to load data from PDF files, specifically invoices, into Weaviate.
- [sql_to_weaviate.ipynb](sql_to_weaviate.ipynb): shows how to import data from a public MySQL database into Weaviate.
- [zendesk_to_weaviate.ipynb](zendesk_to_weaviate.ipynb): loads data from a [Zendesk dlt source](https://dlthub.com/docs/dlt-ecosystem/verified-sources/zendesk) into Weaviate.


### Personio demos

- [personio_demo.ipynb](personio_demo.ipynb): shows how to load data from Personio to duckDB.

### Project demos

Project demos are more extensive compared to the notebook ones and have their own README files. Refer to each project for more details.


## License

This repository is licensed under the [Apache License 2.0](LICENSE.txt). Please refer to the `LICENSE.txt` file for more details.

Happy coding and data loading! 🚀📊
