import time
import traceback

import dlt
import pendulum
import requests
from pydantic import BaseModel
from restack_ai.function import function, log
from dlt.destinations.adapters import weaviate_adapter



class PipelineInput(BaseModel):
    destination: str


@function.defn()
async def anime_pipeline(input: PipelineInput) -> str:
    @dlt.resource(table_name="anime", write_disposition="merge", primary_key="mal_id")
    def get_anime(
        aired_from=dlt.sources.incremental(
            "aired.from", initial_value="2024-07-01T00:00:00+00:00"
        )
    ):
        yield pagination(
            "anime",
            params={
                "order_by": "start_date",
                "start_date": remove_hms(aired_from.last_value),
                "status": "airing",
            },
        )
    try:
        # Set pipeline name, destination, and dataset name
        pipeline = dlt.pipeline(
            pipeline_name="anime_pipeline",
            destination=input.destination,
            dataset_name="anime_data",
            progress="log",
            dev_mode=False,
        )

        data = get_anime().add_limit(2)

        if input.destination == "weaviate":
            data = weaviate_adapter(
                data,
                vectorize=["title", "synopsis"],
            )

        # Run the pipeline using the defined resource
        pipeline.run(data)
        return str(pipeline.last_trace)
    except Exception as e:
        log.error("Something went wrong!", error=e)
        log.error(traceback.format_exc())
        raise e


def remove_hms(date):
    date_obj = pendulum.parse(date)
    return date_obj.to_date_string()


def pagination(endpoint: str, params: dict):
    has_next_page = True
    page = 1
    while has_next_page:
        # print(page)
        params.update({"page": page})

        response = requests.get(f"https://api.jikan.moe/v4/{endpoint}", params)
        time.sleep(0.5)
        if response.status_code != 200:
            print(endpoint, response.status_code, response.json())
            break

        if "data" in response.json():
            yield response.json()["data"]
        if "pagination" in response.json():
            has_next_page = response.json()["pagination"]["has_next_page"]
            page += 1
        else:
            print(endpoint, response.json())
            break
