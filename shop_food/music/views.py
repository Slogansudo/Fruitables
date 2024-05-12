from django.db.transaction import atomic
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Album, Songs
from .serializers import ArtistSerializer, AlbumSerializer, SongsSerializer
from rest_framework import status, filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import LimitOffsetPagination


class ArtistAPIViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'name']

    @action(detail=True, methods=['GET'])
    def check_famous(self, request, *args, **kwargs):
        artist = self.get_object()
        album = Album.objects.filter(artist=artist)
        count = album.count()
        with atomic():
            if count >= 2:
                artist.famous_rating = True
                artist.save()
                return Response(data=artist.famous_rating)
            else:
                return Response(data=artist.famous_rating)

    @action(detail=False, methods=['GET'])
    def top_famous(self, request, *args, **kwargs):
        artists = self.get_queryset()
        artists = artists.filter(famous_rating=True)
        serializer = ArtistSerializer(artists, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET'])
    def re_order(self, request, *args, **kwargs):
        artists = self.get_queryset()
        artists = artists.order_by('-id')
        serializer = ArtistSerializer(artists, many=True)
        return Response(data=serializer.data)


class AlbumAPIViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated, ]
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'title', 'artist__name']

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        albums = self.get_queryset()
        albums = albums.order_by('-rating')[:2]
        serializer = AlbumSerializer(albums, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['GET'])
    def artist(self, request, *args, **kwargs):
        album = self.get_object()
        artist = album.artist
        serializer = ArtistSerializer(artist)
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET'])
    def re_order(self, request, *args, **kwargs):
        album = self.get_queryset()
        album = album.order_by('-id')
        serializer = AlbumSerializer(album, many=True)
        return Response(data=serializer.data)


class SongsAPIViewSet(ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    permission_classes = [IsAuthenticated, ]
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'album__title', 'album__artist__name']

    @action(detail=True, methods=["GET"])
    def listen(self, request, *args, **kwargs):
        songs = self.get_object()
        with atomic():
            songs.listened += 1
            songs.save()
            return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"])
    def top(self, request, *args, **kwargs):
        songs = self.get_queryset()
        songs = songs.order_by('-listened')[:3]
        serializer = SongsSerializer(songs, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=["GET"])
    def album(self, request, *args, **kwargs):
        songs = self.get_object()
        album = songs.album
        serializer = AlbumSerializer(album)
        return Response(data=serializer.data)

    @action(detail=True, methods=["GET"])
    def artist(self, request, *args, **kwargs):
        songs = self.get_object()
        artist = songs.album.artist
        serializer = ArtistSerializer(artist)
        return Response(data=serializer.data)
