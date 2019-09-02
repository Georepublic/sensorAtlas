from .models import Datastream, Thing, Sensor, Location, \
    ObservedProperty, Observation, HistoricalLocation, FeatureOfInterest
from rest_framework import serializers
from .mixins import Expand, Select, ResultFormat, ControlInformation
from .errors import Conflicts


class FeatureOfInterestSerializer(ControlInformation, Expand, ResultFormat, Select):
    """
    Serializer for the nested Features of Interest
    of the Datastreams entity.
    """
    selfLink = serializers.SerializerMethodField()
    navigationLinks = serializers.SerializerMethodField()

    class Meta:
        model = FeatureOfInterest
        fields = (
            'id',
            'selfLink',
            'navigationLinks',
            'name',
            'description',
            'encodingType',
            'feature',
        )

        def get_expandable_fields(*args):
            expandable_fields = {
                'Observations': (
                    ObservationSerializer,
                    (),
                    {'many': True}
                ),
            }
            Conflicts.conflicts.append('FeaturesOfInterest')
            for a in args:
                if a in Conflicts.conflicts:
                    expandable_fields.pop(a, expandable_fields)
                if a not in Conflicts.conflicts:
                    Conflicts.conflicts.append(a)
            return expandable_fields


class HistoricalLocationSerializer(ControlInformation, Expand, ResultFormat, Select):
    """
    Serializer for the nested Historical Locations of the
    Datastreams entity.
    """
    selfLink = serializers.SerializerMethodField()
    navigationLinks = serializers.SerializerMethodField()

    class Meta:
        model = HistoricalLocation
        fields = (
            'id',
            'selfLink',
            'navigationLinks',
            'time'
        )

        def get_expandable_fields(*args):
            expandable_fields = {
                'Thing': (ThingSerializer),
                'Locations': (
                    LocationSerializer,
                    (),
                    {'many': True}
                )
            }
            Conflicts.conflicts.append('HistoricalLocations')
            for a in args:
                if a in Conflicts.conflicts:
                    expandable_fields.pop(a, expandable_fields)
                if a not in Conflicts.conflicts:
                    Conflicts.conflicts.append(a)
            return expandable_fields


class LocationSerializer(ControlInformation, Expand, ResultFormat, Select):
    """
    Serializer for the nested Locations of the Datastreams entity.
    """
    selfLink = serializers.SerializerMethodField()
    navigationLinks = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = (
            'id',
            'selfLink',
            'navigationLinks',
            'name',
            'description',
            'encodingType',
            'location'
        )

        def get_expandable_fields(*args):
            expandable_fields = {
                'Things': (
                    ThingSerializer,
                    (),
                    {'many': True}
                    ),
                'HistoricalLocations': (
                    HistoricalLocationSerializer,
                    (),
                    {'many': True}
                    )
            }
            Conflicts.conflicts.append('Locations')
            for a in args:
                if a in Conflicts.conflicts:
                    expandable_fields.pop(a, expandable_fields)
                if a not in Conflicts.conflicts:
                    Conflicts.conflicts.append(a)
            return expandable_fields


class ThingSerializer(ControlInformation, Expand, ResultFormat, Select):
    """
    Serializer for the nested Things of the Datastreams entity.
    """
    selfLink = serializers.SerializerMethodField()
    navigationLinks = serializers.SerializerMethodField()

    class Meta:
        model = Thing
        fields = (
            'id',
            'selfLink',
            'navigationLinks',
            'name',
            'description',
            'properties'
        )

        def get_expandable_fields(*args):
            expandable_fields = {
                'Datastreams': (
                    DatastreamSerializer,
                    (),
                    {'many': True}
                ),
                'Locations': (
                    LocationSerializer,
                    (),
                    {'many': True}
                ),
                'HistoricalLocations': (
                    HistoricalLocationSerializer,
                    (),
                    {'many': True}
                )
            }
            Conflicts.conflicts.append('Things')
            for a in args:
                if a in Conflicts.conflicts:
                    expandable_fields.pop(a, expandable_fields)
                if a not in Conflicts.conflicts:
                    Conflicts.conflicts.append(a)
            return expandable_fields


class SensorSerializer(ControlInformation, Expand, ResultFormat, Select):
    """
    Serializer for the nested Sensors of the Datastreams entity.
    """
    selfLink = serializers.SerializerMethodField()
    navigationLinks = serializers.SerializerMethodField()

    class Meta:
        model = Sensor
        fields = (
            'id',
            'selfLink',
            'navigationLinks',
            'name',
            'description',
            'encodingType',
            'metadata'
            )

        def get_expandable_fields(*args):
            expandable_fields = {
                'Datastream': (
                    DatastreamSerializer,
                    (),
                    {'many': True}
                )
            }
            Conflicts.conflicts.append('Sensors')
            for a in args:
                if a in Conflicts.conflicts:
                    expandable_fields.pop(a, expandable_fields)
                if a not in Conflicts.conflicts:
                    Conflicts.conflicts.append(a)
            return expandable_fields


class ObservedPropertySerializer(ControlInformation, Expand, ResultFormat, Select):
    """
    Serializer for the nested Observed Properties of the
    Datastreams entity.
    """
    selfLink = serializers.SerializerMethodField()
    navigationLinks = serializers.SerializerMethodField()

    class Meta:
        model = ObservedProperty
        fields = (
            'id',
            'selfLink',
            'navigationLinks',
            'name',
            'definition',
            'description'
        )

        def get_expandable_fields(*args):
            expandable_fields = {
                'Datastream': (
                    DatastreamSerializer,
                    (),
                    {'many': True}
                )
            }
            Conflicts.conflicts.append('ObservedProperties')
            for a in args:
                if a in Conflicts.conflicts:
                    expandable_fields.pop(a, expandable_fields)
                if a not in Conflicts.conflicts:
                    Conflicts.conflicts.append(a)
            return expandable_fields


class ObservationSerializer(ControlInformation, Expand, ResultFormat, Select):
    """
    Serializer for the nested Observations of the Datastreams entity.
    """
    selfLink = serializers.SerializerMethodField()
    navigationLinks = serializers.SerializerMethodField()

    class Meta:
        model = Observation
        fields = (
            'id',
            'selfLink',
            'navigationLinks',
            'phenomenonTime',
            'result',
            'resultTime'
        )

        def get_expandable_fields(*args):
            expandable_fields = {
                'Datastream': (DatastreamSerializer),
                'FeatureOfInterest': (FeatureOfInterestSerializer),
            }
            Conflicts.conflicts.append('Observations')
            for a in args:
                if a in Conflicts.conflicts:
                    expandable_fields.pop(a, expandable_fields)
                if a not in Conflicts.conflicts:
                    Conflicts.conflicts.append(a)
            return expandable_fields


class DatastreamSerializer(ControlInformation, Expand, ResultFormat, Select):
    """
    Base serializer for the Datastreams entity.
    """
    selfLink = serializers.SerializerMethodField()
    navigationLinks = serializers.SerializerMethodField()

    class Meta:
        model = Datastream
        fields = (
            'id',
            'selfLink',
            'navigationLinks',
            'name',
            'description',
            'unitOfMeasurement',
            'observationType',
            'observedArea',
            'phenomenonTime',
            'resultTime',
        )

        def get_expandable_fields(*args):
            expandable_fields = {
                'Thing': (ThingSerializer),
                'Sensor': (SensorSerializer),
                'ObservedProperty': (ObservedPropertySerializer),
                'Observations': (
                    ObservationSerializer,
                    (),
                    {'many': True}
                )
            }
            Conflicts.conflicts.append('Datastreams')
            for a in args:
                if a in Conflicts.conflicts:
                    expandable_fields.pop(a, expandable_fields)
                if a not in Conflicts.conflicts:
                    Conflicts.conflicts.append(a)
            return expandable_fields
