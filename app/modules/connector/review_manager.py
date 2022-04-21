import os

import gitlab
from dotenv import load_dotenv

load_dotenv()


class ReviewManager:
    client = gitlab.Gitlab(os.environ.get('GITLAB_URL'), private_token=os.environ.get('GITLAB_TOKEN'))

    def assign_reviewer(self, project_id, merge_request_id, reviewer_id=70755):
        """ Assigns a reviewer to a merge request. """
        project = self.client.projects.get(project_id)
        mr = project.mergerequests.get(merge_request_id)
        # id 70755 - Ivan Golikov | Hardcoded for now
        mr.manager.update(mr.get_id(), {'reviewer_ids': [reviewer_id]})


    def retrieve_viewger_team(self):
        """ Temporary method to retrieve the info of viewger team. """
        # gets a viewger project -> Project obj
        viewger_project = self.client.projects.get(id=131110)
        # gets a list of all team members within viewger repo
        team = viewger_project.members.list()
        # prints out all team members and their ids
        for member in team:
            print(member.id, member.username)
        # get a list of MRs opened in viewger repo
        mrs = viewger_project.mergerequests.list(state='opened')
        # prints out all MRs, their ids and assigned reviewer
        for mr in mrs:
            print(mr.id, mr.title, mr.get_id())
            print(mr.reviewers)

test = ReviewManager()
test.retrieve_viewger_team()
