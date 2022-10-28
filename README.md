## App Runner Leaderboard Backend
Note: This is not Production grade and simply meant as a demo

## Description
We will be setting up a leaderboard application which is comprised of two microservices hosted on App Runner. The first microservice is a frontend UI application which has a public endpoint and the second microservice is a backend application which has a private endpoint. The frontend application communicates with the backend application to retrieve leaderboard data. The backend application retrieves the leaderboard data by communicating with an ElastiCache DB in a VPC. 

* Frontend: https://github.com/aws-samples/apprunner-leaderboard-frontend 
* Backend: https://github.com/aws-samples/apprunner-leaderboard-backend

## AWS Services
1. App Runner
2. Elasticache Redis

## Teardown Instructions
Go to App Runner console and delete the service.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

