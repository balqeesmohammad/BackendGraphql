import graphene
import musicapp.schema

class Query(musicapp.schema.Query, graphene.ObjectType):
	pass

# class Mutation(musicapp.schema.Mutation, graphene.ObjectType):
# 	pass

schema = graphene.Schema(query=Query)


# , mutation=Mutation