import asyncio

from upload_data.upload import run_upload


if __name__ == "__main__":
    """Entry point for uploading data"""
    asyncio.run(run_upload())
