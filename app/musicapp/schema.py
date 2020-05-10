import graphene
from graphene_django import DjangoObjectType
from .models import Artist, Album, Song


class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist
        # only_fields = ('name', 'id')


class AlbumType(DjangoObjectType):
    class Meta:
        model = Album
        only_fields = ('albumname', 'artist', 'id')

class SongType(DjangoObjectType):
    class Meta:
        model = Song
        #only_fields = ('songtitle', 'album', 'id')




class Query(graphene.ObjectType):
    artists = graphene.List(ArtistType)
    albums = graphene.List(AlbumType)
    songs = graphene.List(SongType)




    def resolve_artists(self, info):
    	return Artist.objects.all()

    def resolve_albums(self, info):
    	return Album.objects.all()

    def resolve_songs(self, info):
    	return Song.objects.all()



class CreateArtist(graphene.Mutation):
    artist = graphene.Field(ArtistType)

    class Arguments:
    	name = graphene.String(required=True)

    def mutate(self, info, name):
        artist = Artist(name=name)
        artist.save()
        return CreateArtist(artist=artist)



# class CreateAlbum(graphene.Mutation):
#     albumm = graphene.Field(AlbumType)
#     artist = graphene.Field(ArtistType)

#     class Arguments:
#     	artist_id = graphene.Int(required=True)
#     	albumname = graphene.String(required=True)


#     def mutate(self, info, artist_id, albumname):
#         #
#         artist = Artist.objects.get(id=artist_id)
#         if not artist:
#         	raise Exception('cannot find artist with given artist id')
#         albumm = Album(albumname=albumname)
#         Album.objects.create(
#         	albumm=albumm,
#         	artist=artist
#         	)
#         return CreateAlbum(artist=artist, albumm=albumm)

# class CreateSong(graphene.Mutation):
# 	songtitles = graphene.Field(SongType)
# 	album = graphene.Field(AlbumType)
# 	class Arguments:
# 		album_id = graphene.Int(required=True)
# 		#songtitle = graphene.NonNull(graphene.String)
# 		songtitles = graphene.NonNull(graphene.String)

# 	def mutate(self, info, album_id, songtitle):
# 	   	songtitles = Song(songtitle=songtitle)
# 	album = Album.objects.get(id=album_id)
# 	if not album:
# 			raise Exception('cannot find album with given album id')
	    
#     Song.objects.create(
    	
#     	songtitles=songtitles,
#     	album=album
#     	)
# 	    return CreateSong(album=album, songtitles=songtitles)

# class Mutation(graphene.ObjectType):
#     create_artist = CreateArtist.Field()
#     Create_album = CreateAlbum.Field()
#     Create_song = CreateSong.Field()
#         