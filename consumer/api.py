"""Module for APIs"""

from django.shortcuts import get_object_or_404
from rest_framework import viewsets  # For routers
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response

from consumer import models, serializers