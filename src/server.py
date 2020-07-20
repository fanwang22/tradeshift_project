import flask
from flask import request, jsonify, abort
import tree_functions
from tree import *

app = flask.Flask(__name__)

# create the tree document and keep it around for the app
tree = Tree()

@app.route('/', methods=['GET'])
def home():
    return "<h1>Tradeshift</h1><p>Tree Project</p> "

@app.route('/api/get_descendants', methods=['GET'])
def descendants():
    global tree
    try:
        id = request.args['id']
    except KeyError:
        # log error to a log file
        error_message = 'Invalid arg'
        print(error_message)
        abort(404, error_message)
    if id in tree.tree_map:
        return tree_functions.get_descendant(tree.tree_map[id])
    else:
        error_message = 'Node id ' + id + ' is not found'
        print(error_message)
        abort(404, error_message)

@app.route('/api/change_parent', methods=['PUT'])
def change_parent():
    global tree

    content = request.get_json()
    try:
        node_id = content["node_id"]
    except KeyError:
        error_message = 'node_id not provided'
        abort(404, error_message)

    try:
        parent_id = content["parent_id"]
    except KeyError:
        error_message = 'parent_id not provided'
        abort(404, error_message)

    if node_id not in tree.tree_map:
        error_message = 'node_id not found'
        abort(404, error_message)

    if parent_id not in tree.tree_map:
        error_message = 'parent_id not found'
        abort(404, error_message)

    tree.root = tree_functions.change_parent(tree.root, node_id, parent_id)

    return 'Parent has been changed'

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e)), 404

app.run()