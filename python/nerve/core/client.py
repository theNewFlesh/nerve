#! /usr/bin/env python
import os
import yaml
import json
from copy import deepcopy
from itertools import *
from github3 import login
from github3.repos.branch import Branch
from github3.null import NullObject
# ------------------------------------------------------------------------------

# TODO: added waiting and timeout logic
# TODO: handle github errors

'''
The model module contains the Client class, nerve's internal API for accessing Github

Platforrm:
    Unix

Author:
    Alex Braun <alexander.g.braun@gmail.com> <http://www.alexgbraun.com>
'''

class Client(object):
    '''
    Class for interacting with a single repository on Github

    Attributes:
        config (dict): a dictionary representing Nerve's internal configuration

    API: has_branch, set_default_branch, add_team
         create_pull_request, merge_pull_request, delete
    '''
    def __init__(self, config):
        '''
        Client constructor creates and acts as a single repository on Github

        Args:
            config (dict): a nerve project configuration (derived from nerverc)

        Returns:
            Client: Github repository
        '''
        if isinstance(config, str):
            with open(config, 'r') as f:
                config = yaml.load(f)

        self._client = login(config['username'], token=config['token'])
        self._org = self._client.organization(config['organization'])
        self._team_ids = {team.name: team.id for team in self._org.teams()}
        self._repo = self._create_repository(
            config['name'],
            config['organization'],
            config['private']
        )

        if config['url-type'] == 'ssh':
            config['url'] = self._repo.ssh_url
        elif config['url-type'] == 'http':
            config['url'] = self._repo.http_url
        config['fullname'] = self._repo.full_name
        config['id'] = self._repo.id

        self._config = config

    def __getitem__(self, key):
        return self._config[key]

    def _create_repository(self, name, orgname, private):
        '''
        Creates a repository on GitHub

        Args:
            name (str): repository name
            organme (str): GitHub organization name
            private (bool): repository availability

        Returns:
            github3.repos.repo.Repository
        '''
        repo = self._client.repository(orgname, name)
        if isinstance(repo, NullObject):
            repo = self._org.create_repository(
                name,
                private=private
            )
        return repo
    # --------------------------------------------------------------------------

    @property
    def config(self):
        '''
        Returns a copy of this object's configuration

        Returns:
            dict: internal configuration
        '''
        return deepcopy(self._config)

    # def create_branch(self, name):
    #     # github3 has no ability to create a branch
    #     if self.has_branch(name, wait=True):
    #         return True

    def has_branch(self, name):
        '''
        Checks whether Github repository has a given branch

        Args:
            name (str): branch name

        Returns:
            bool: branch status
        '''
        return isinstance(self._repo.branch(name), Branch)

    def set_default_branch(self, name):
        '''
        Sets default branch of GitHub repository

        Args:
            name (str): branch name

        Returns:
            bool: success status
        '''
        self._repo.edit(self['name'], default_branch=name)
        return True

    def add_team(self, name, permission):
        '''
        Checks whether Github repository has a given branch

        Args:
            name (str): branch name
            permission (str): team permissions. Values include: read, write, pull, push

        Returns:
            bool: success status
        '''
        # add_repository is fixed in develop branch of gihub3
        # making this code obsolete
        lut = dict(
            read='pull',
            write='push',
            pull='pull',
            push='push'
        )
        perm = lut[permission]
        perm = {'permission': perm}

        id_ = self._team_ids[name]
        team = self._org.team(id_)
        url = team._build_url('repos', self['fullname'], base_url=team._api)
        return team._boolean(team._put(url, data=json.dumps(perm)), 204, 404)

    def create_pull_request(self, title, base, branch, body=None):
        '''
        Creates a pull request to merge a head commit of branch into a base branch on Github

        Args:
            title (str): title of pull request
            base (str): branch to merge head into
            branch (str): branch to be merged
            body (str): markdown formatted string to put in the comments

        Returns:
            int: pull request number
        '''
        head = self._repo.branch(branch).commit.sha
        request = self._repo.create_pull(title, base, head, body=body)
        return request.number

    def merge_pull_request(self, number, message=''):
        '''
        Merges a given pull request on GitHub

        Args:
            number (int): pull request number
            message (str, optional): commit message. Default: ''

        Returns:
            bool: success status
        '''
        return self._repo.pull_request(number).merge(message)

    def delete(self):
        '''
        Deletes repository off of Github

        Returns:
            bool: success status
        '''
        self._repo.delete()
        return True
# ------------------------------------------------------------------------------

def main():
    '''
    Run help if called directly
    '''

    import __main__
    help(__main__)
# ------------------------------------------------------------------------------

__all__ = ['Client']

if __name__ == '__main__':
    main()