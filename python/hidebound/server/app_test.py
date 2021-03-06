import os
from pathlib import Path
from tempfile import TemporaryDirectory

import lunchbox.tools as lbt

from hidebound.core.database_test_base import DatabaseTestBase
import hidebound.server.app as application
import hidebound.server.components as components
import hidebound.server.server_tools as server_tools
# ------------------------------------------------------------------------------


class AppTests(DatabaseTestBase):
    def setUp(self):
        # setup files and dirs
        self.tempdir = TemporaryDirectory()
        temp = self.tempdir.name
        self.hb_root = Path(temp, 'hidebound').as_posix()
        os.makedirs(self.hb_root)

        self.root = Path(temp, 'projects').as_posix()
        os.makedirs(self.root)

        self.create_files(self.root)

        # setup app
        self.context = application.APP.server.app_context()
        self.context.push()

        self.app = self.context.app

        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

        self.specs = lbt.relative_path(
            __file__,
            '../core/test_specifications.py'
        ).absolute().as_posix()

    def tearDown(self):
        self.context.pop()
        self.tempdir.cleanup()

    def test_serve_stylesheet(self):
        params = dict(
            COLOR_SCHEME=components.COLOR_SCHEME,
            FONT_FAMILY=components.FONT_FAMILY,
        )
        expected = server_tools.render_template('style.css.j2', params)
        result = next(self.client.get('/static/style.css').response)
        self.assertEqual(result, expected)
