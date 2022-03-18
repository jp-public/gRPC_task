from concurrent import futures

import grpc
import sys
from proto import restaurant_pb2
from proto import restaurant_pb2_grpc

RESTAURANT_ITEMS_FOOD = ["chips", "fish", "burger", "pizza", "pasta", "salad"]
RESTAURANT_ITEMS_DRINK = ["water", "fizzy drink", "juice", "smoothie", "coffee", "beer"]
RESTAURANT_ITEMS_DESSERT = ["ice cream", "chocolate cake", "cheese cake", "brownie", "pancakes", "waffles"]


class Restaurant(restaurant_pb2_grpc.RestaurantServicer):

    def FoodOrder(self, request, context):
        order_status = "REJECTED"
        if all(x in RESTAURANT_ITEMS_FOOD for x in request.items):
            order_status = "ACCEPTED"
        return restaurant_pb2.RestaurantResponse(orderID=request.orderID, status=order_status)

    def DrinkOrder(self, request, context):
        order_status = "REJECTED"
        if all(x in RESTAURANT_ITEMS_DRINK for x in request.items):
            order_status = "ACCEPTED"
        return restaurant_pb2.RestaurantResponse(orderID=request.orderID, status=order_status)

    def DessertOrder(self, request, context):
        order_status = "REJECTED"
        if all(x in RESTAURANT_ITEMS_DESSERT for x in request.items):
            order_status = "ACCEPTED"
        return restaurant_pb2.RestaurantResponse(orderID=request.orderID, status=order_status)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    restaurant_pb2_grpc.add_RestaurantServicer_to_server(Restaurant(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
