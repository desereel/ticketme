from django.db import models
from django.urls import reverse 	# Used to generate URLS by reversing the URL patterns
import uuid 						# Required for unique concert instances

# Create your models here.

class Concert(models.Model):
	
	"""Model representing a concert (but not a specific concert)."""

	name = models.CharField(max_length=200)

	# Foreign Key used because concert can only have one main act, but acts can have multiple concerts

	act = models.ForeignKey('Act', on_delete=models.SET_NULL, null=True)

	summary = models.TextField(max_length=1000, help_text='Enter a brief description of the concert')

	def __str__(self):
		"""String for representing the Model object."""
		return self.name

	def get_absolute_url(self):
		"""Returns the URL to access a detail record for this concert."""
		return reverse('concert-detail', args=[str(self.id)])

class ConcertInstance(models.Model):

	"""Model representing a specific concert"""
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular concert within the database')
	concert = models.ForeignKey('Concert', on_delete=models.RESTRICT, null=True)
	
	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.id} ({self.concert.name})'

class Act(models.Model):
	
	"""Model representing an act."""
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	class Meta:
		ordering = ['last_name', 'first_name']
	
	def get_absolute_url(self):
		"""Returns the URL to access a particular act instance."""
		return reverse('act-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model objext."""
		return f'{self.last_name}, {self.first_name}'
