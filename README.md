## Description:

Created the project using Python Flask. The server code will be running on http://127.0.0.1:5000  <br /> 
Each tree node has an id which is used to be referenced in the APIs. More details about the tree node structure can be found in src/tree_node.py  <br /> 
When the web server starts, a tree strucutre will be created, like this:  <br /> 
```
         root
        /    \ 
       a      b  
       | 
       c 
```
the values of the nodes are shown while id of root is '1', id of a is '2', id of b is '3' and id of c is '4'  <br /> 
A hashmap (dictionary in python) is built as well for quick search, more details about the tree can be found in src/tree.py

## To launch the project:

- Install python3 (create a virtualenv is optional)
- Install dependencies by running: 
      `pip3 install -r requirements.txt`
- Start the web server by running: 
      `./server.py`

## To use APIs:
- Get all descendant nodes of a given node
    Use the endpoint with the node id: http://127.0.0.1:5000/api/get_descendants?id=3. 
    it will return all its descendants

- Change the parent node of a given node
    Use curl or postman to send a PUT request to the endpoint: http://127.0.0.1:5000/api/change_parent
    with the json data like this: 
    ```
    {
      "node_id": "4",
      "parent_id": "2"
    }
    ```
    You can use the get_descendats API to verify the change
