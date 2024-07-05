#!/bin/bash

echo "Filling user pool with 3 users..."
response=$(curl -s -X GET "http://localhost:5001/api/user-pool?fill=3")
echo "Response: $response"

echo "Listing all unused users..."
response=$(curl -s -X GET http://localhost:5001/api/user/list)
echo "Response: $response"

echo "Getting an unused user..."
response=$(curl -s -X GET http://localhost:5001/api/user)
echo "Response: $response"

echo "Listing remaining unused users..."
response=$(curl -s -X GET http://localhost:5001/api/user/list)
echo "Response: $response"

echo "Filling user pool with 50 users..."
response=$(curl -s -X GET "http://localhost:5001/api/user-pool?fill=50")
echo "Response: $response"

echo "Listing all unused users after filling the pool..."
response=$(curl -s -X GET http://localhost:5001/api/user/list)
echo "Response: $response"

echo "Flushing all users from the pool..."
response=$(curl -s -X GET "http://localhost:5001/api/user-pool?flush=true")
echo "Response: $response"

echo "Listing all unused users after flushing the pool..."
response=$(curl -s -X GET http://localhost:5001/api/user/list)
echo "Response: $response"