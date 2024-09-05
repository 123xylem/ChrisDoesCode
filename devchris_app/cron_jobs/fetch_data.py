import time
import logging
from django_cron import CronJobBase, Schedule
from code_app.code_submissions import retrieveSubmissionMetaFromLeetCode, retrieveSubmissionsFromRepo, retrieveLeetMetaStats
logger = logging.getLogger(__name__)
logging.shutdown()

class FetchSubmissionsCronJob(CronJobBase):
    RUN_EVERY_MINS = 2500 #every 2 days

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'devchris_app.fetchSubmissions'

    def do(self):
        logger.info(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())}]  FetchSubmissionsCronJob started!")
        try:
            sub_meta = retrieveSubmissionMetaFromLeetCode()
            time.sleep(10)
            subs = retrieveSubmissionsFromRepo()
            time.sleep(2)
            leet_stats = retrieveLeetMetaStats()
            logger.warning(f"DATA FROM FETCH \n \n Submissions:  {subs} \n Leet Stats: {leet_stats}", exc_info=True)

        except Exception as e:
            logger.error(f"Error fetching data: {str(e)} \n meta: {sub_meta} \n Submissions:  {subs} \n Leet Stats: {leet_stats}", exc_info=True)
            with open('errors.log', 'a') as f:
                f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())}] Error fetching data: {str(e)}\n")

