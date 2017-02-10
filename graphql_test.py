import graphene

class Query(graphene.ObjectType):
	hello = graphene.String()

	def resolve_hello(self, args,context, info):
		return "hello world"



schema = graphene.schema(query=Query)
result = schema.excute('{hello}')
print(result.data['hello'])