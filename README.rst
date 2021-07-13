"django-tracks" project
=======================

A basic Django project used to provide a sample database for test purposes.

A specific technique is proposed to overcome the limitations of Django inlines
when editing a one-to-many relationship with too many related records.

Although some interesting app are available to paginate the inlines
(for example: `Django Admin Inline Paginator <https://github.com/shinneider/django-admin-inline-paginator>`_),
a possible alterntive is to restrict the changelist for child records based on a specific parent record.


Restrict the changelist for child records based on a specific parent records' value
-----------------------------------------------------------------------------------

The advantages of this approach are:

- you have better tools to navigate the child records subset, using familiar
  pagination, search, filter, date hierarchy and other widgets
- you can use a full-page change view to edit a specific child record

Unfortunately, some code from django.contrib.admin.ModelAdmin has to be duplicated,
although a simple refactoring could be in principle applyied to avoid this.

