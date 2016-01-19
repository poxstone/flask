from tumblelog.models import *
post = Post(
	title="Hello World!",
	slug="hello-world",
	body="Welcome to my new shiny Tumble log powered by MongoDB, MongoEngine, and Flask"
)
post.save()