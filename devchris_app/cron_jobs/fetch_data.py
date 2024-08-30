import time
import logging
from django_cron import CronJobBase, Schedule
from code_app.code_submissions import retrieveSubmissionMetaFromLeetCode, retrieveSubmissionsFromRepo
logger = logging.getLogger(__name__)

class FetchSubmissionsCronJob(CronJobBase):
    RUN_EVERY_MINS = .5  # Run every minute

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'devchris_app.fetchSubmissions'

    def do(self):
        logger.info('FetchSubmissionsCronJob started!')
        try:
            retrieveSubmissionMetaFromLeetCode()
            time.sleep(10)
            retrieveSubmissionsFromRepo(20)
        except Exception as e:
            logger.error(f"Error fetching data: {str(e)}", exc_info=True)
            with open('errors.log', 'a') as f:
                f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())}] Error fetching data: {str(e)}\n")

