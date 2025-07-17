 RESTFUL - web services are services that follow REST architecture. REST stands for Representational State Transfer and uses HTTP protocol (web protocol) for implementation. These services are lightweight, provide maintainability, scalability, support communication among multiple applications that are developed using different programming languages. They provide means of accessing resources present at server required for the client via the web browser by means of request headers, request body, response body, status codes, et



REST Resource - Every content in the REST architecture is considered a resource. The resource is analogous to the object in the object-oriented programming world. They can either be represented as text files, HTML pages, images, or any other dynamic data. The REST Server provides access to these resources whereas the REST client consumes (accesses and modifies) these resources. Every resource is identified globally by means of a URI.
URI? - Uniform Resource Identifier is the full form of URI which is used for identifying each resource of the REST architecture. URI is of the format:
URN: Uniform Resource Name identifies the resource by means of a name that is both unique and persistent.
URL - has the information regarding fetching of a resource from its location.


Features of RESTful Web Services?
The service is based on the Client-Server model.
The service uses HTTP Protocol for fetching data/resources, query execution, or any other functions.
The medium of communication between the client and server is called “Messaging”.
Resources are accessible to the service by means of URIs.
It follows the statelessness concept where the client request and response are not dependent on others and thereby provides total assurance of getting the required data.
These services also use the concept of caching to minimize the server calls for the same type of repeated requests.
These services can also use SOAP services as implementation protocol to REST architectural pattern.

Disadvantages of RESTful web services?
As the services follow the idea of statelessness, it is not possible to maintain sessions. (Session simulation responsibility lies on the client-side to pass the session id)
REST does not impose security restrictions inherently. It inherits the security measures of the protocols implementing it. Hence, care must be chosen to implement security measures like integrating SSL/TLS based authentications, etc.

Statelessness in REST-  The REST architecture is designed in such a way that the client state is not maintained on the server. This is known as statelessness. The context is provided by the client to the server using which the server processes the client’s request. The session on the server is identified by the session identifier sent by the client.

Messaging -  technique of sending a message from the REST client to the REST server in the form of an HTTP request and the server responding back with the response as HTTP Response

Differentiate between SOAP and REST?
SOAP 	REST
SOAP - Simple Object Access Protocol 	REST - Representational State Transfer
SOAP is a protocol used to implement web services.	REST is an architectural design pattern for developing web services
SOAP cannot use REST as it is a protocol.	REST architecture can have SOAP protocol as part of the implementation.
SOAP specifies standards that are meant to be followed strictly.	REST defines standards but they need not be strictly followed.
SOAP client is more tightly coupled to the server which is similar to desktop applications having strict contracts.	The REST client is more flexible like a browser and does not depend on how the server is developed unless it follows the protocols required for establishing communication.
SOAP supports only XML transmission between the client and the server.	REST supports data of multiple formats like XML, JSON, MIME, Text, etc.
SOAP reads are not cacheable.	REST read requests can be cached.
SOAP uses service interfaces for exposing the resource logic.	REST uses URI to expose the resource logic.
SOAP is slower.	REST is faster.
Since SOAP is a protocol, it defines its own security measures.	REST only inherits the security measures based on what protocol it uses for the implementation.
SOAP is not commonly preferred, but they are used in cases which require stateful data transfer and more reliability.	REST is commonly preferred by developers these days as it provides more scalability and maintainability.

URI for web services, what are the best practices that needs to be followed?
While defining resources, use plural nouns. Example: To identify user resource, use the name “users” for that resource.
While using the long name for resources, use underscore or hyphen. Avoid using spaces between words. For example, to define authorized users resource, the name can be “authorized_users” or “authorized-users”.
The URI is case-insensitive, but as part of best practice, it is recommended to use lower case only.
While developing URI, the backward compatibility must be maintained once it gets published. When the URI is updated, the older URI must be redirected to the new one using the HTTP status code 300.
Use appropriate HTTP methods like GET, PUT, DELETE, PATCH, etc. It is not needed or recommended to use these method names in the URI. Example: To get user details of a particular ID, use /users/{id} instead of /getUser
Use the technique of forward slashing to indicate the hierarchy between the resources and the collections. Example: To get the address of the user of a particular id, we can use: /users/{id}/address



What are the best practices to develop RESTful web services?
Develop REST APIs that accept and responds with JSON data format whenever possible. This is because a majority of the client and server technologies have inbuilt support to read and parse JSON objects with ease.
To ensure that the application responds using JSON data format, the response header should have Content-Type set to as application/JSON, this is because certain HTTP clients look at the value of this response header to parse the objects appropriately.
To ensure that the request sends the data in JSON format, again the Content-Type must be set to application/JSON on the request header.
While naming the resource endpoints, ensure to use plural nouns and not verbs. The API endpoints should be clear, brief, easy to understand, and informative. 
To represent the hierarchy of resources, use the nesting in the naming convention of the endpoints. In case, you want to retrieve data of one object residing in another object, the endpoint should reflect this to communicate what is happening. For example, to get the address of an author, we can use the GET method for the URI /authors/:id/address'
Please ensure there are no more than 2 or 3 levels of nesting as the name of the URI can become too long and unwieldy.
Error Handling should be done gracefully by returning appropriate error codes the application has encountered. 
While retrieving huge resource data, it is advisable to include filtering and pagination of the resources. This is because returning huge data all at once can slow down the system and reduce the application performance.Pagination of data is done to ensure only some results are sent at a time. Doing this can increase the server performance and reduce the burden of the server resources.
Good security practices are a must while developing REST APIs.  Hence, incorporating SSL/TLS becomes the most important step while developing APIs as they facilitate establishing secure communication. SSL certificates are easier to get and load on the server.
Role-based access controls should be in place to make sure only the right set of users can access the right set of data.
Cache the data in order to improve the application performance. Caching is done to avoid querying the database for a request repeated times. However, care must be taken to ensure that the cache has updated data and not outdated ones. Frequent cache update measures need to be incorporated. There are many cache providers like Redis that can assist in caching.
API Versioning: Versioning needs to be done in case we are planning to make any changes with the existing endpoints. We do not want to break communication between our application and the apps that consume our application while we are working on the API release.

components of HTTP Request?
Method/Verb − This part tells what methods the request operation represents. Methods like GET, PUT, POST, DELETE, etc are some examples.
URI − This part is used for uniquely identifying the resources on the server.
HTTP Version − This part indicates what version of HTTP protocol you are using. An example can be HTTP v1.1.
Request Header − This part has the details of the request metadata such as client type, the content format supported, message format, cache settings, etc.

core components of HTTP Response?
Response Status Code − This represents the server response status code for the requested resource. Example- 400 represents a client-side error, 200 represents a successful response.
HTTP Version − Indicates the HTTP protocol version.
Response Header − This part has the metadata of the response message. Data can describe what is the content length, content type, response date, what is server type, etc.
Response Body − This part contains what is the actual resource/message returned from the server.

What makes REST services to be easily scalable? REST services follow the concept of statelessness which essentially means no storing of any data across the requests on the server. This makes it easier to scale horizontally because the servers need not communicate much with each other while serving requests.

Following are the questions you need to ask to help you decide which service can be used:

Do you want to expose resource data or business logic?
SOAP is commonly used for exposing business logic and REST for exposing data.
Does the client require a formal strict contract?
If yes, SOAP provides strict contracts by using WSDL. Hence, SOAP is preferred here.
Does your service require support for multiple formats of data?
If yes, REST supports multiple data formats which is why it is preferred in this case.
Does your service require AJAX call support?
If yes, REST can be used as it provides the XMLHttpRequest.
Does your service require both synchronous and asynchronous requests?
SOAP has support for both sync/async operations.
REST only supports synchronous calls.
Does your service require statelessness?
If yes, REST is suitable. If no, SOAP is preferred.
Does your service require a high-security level?
If yes, SOAP is preferred. REST inherits the security property based on the underlying implementation of the protocol. Hence, it can’t be preferred at all times.
Does your service require support for transactions?
If yes, SOAP is preferred as it is good in providing advanced support for transaction management.
What is the bandwidth/resource required?
SOAP involves a lot of overhead while sending and receiving XML data, hence it consumes a lot of bandwidth.
REST makes use of less bandwidth for data transmission.
Do you want services that are easy to develop, test, and maintain frequently?
REST is known for simplicity, hence it is preferred.

. How does HTTP Basic Authentication work?
While implementing Basic Authentication as part of APIs, the user must provide the username and password which is then concatenated by the browser in the form of “username: password” and then perform base64 encoding on it. The encoded value is then sent as the value for the “Authorization” header on every HTTP request from the browser. Since the credentials are only encoded, it is advised to use this form when requests are sent over HTTPS as they are not secure and can be intercepted by anyone if secure protocols are not used.







 