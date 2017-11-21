"""
Provides a property DAO object.

Created on 09.05.2016

@author: Alvaro.Ortiz
"""

from rdf2mw.AbstractDAO import AbstractDAO


class DatatypePropertyDAO(AbstractDAO):
    """Provides a property DAO object."""

    def __init__(self, manager):
        """
        Construct.

        Instantiate the DAO class and associate it with a DAO manager,
        which manages the connection.

        @param manager: class implementing AbstractManager
        """
        self._manager = manager
        self.values = {}

    def create(self, sprop, language=None):
        """Override abstract method."""
        # markdown goes in the MediaWiki page
        markdown = ""
        if sprop.getComment(language):
            markdown += "''%s''\n\n" % sprop.getComment(language)

        datatype = "Text"  # default
        if sprop.range == "dateTime":
            datatype = "Date"
        elif sprop.range == "boolean":
            datatype = "Boolean"
        elif sprop.range == "string":
            datatype = "Text"
        elif sprop.range == "DataOneOf":
            datatype = "Text"

        markdown += "This is a property of type [[Has type::%s]].\n" % datatype

        if sprop.range == "DataOneOf" or sprop.range == "boolean":
            markdown += "The allowed values for this property are:\n"
            for item in sprop.allowedValues:
                markdown += "[[Allows value::%s]]\n" % item

        self.values['property'] = markdown

        # Send to MediaWiki
        self._manager.commit(sprop.name, self.values)

    def delete(self, sprop):
        """Override abstract method."""
        pages = ['property']

        # Send to MediaWiki
        self._manager.delete(sprop.name, pages)

    def getValues(self):
        """Override abstract method."""
        return self.values