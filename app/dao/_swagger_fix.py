# fix error  'cached_property' from 'werkzeug'
import werkzeug
from flask.scaffold import _endpoint_from_view_func
from werkzeug.utils import cached_property
import flask

flask.helpers._endpoint_from_view_func = _endpoint_from_view_func
werkzeug.cached_property = cached_property
