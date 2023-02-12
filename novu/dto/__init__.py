"""This module is used to gather all Data Transfer Object definitions in the Novu SDK.

All definitions of format returned by the Novu API are here, which help us to instantiate and document them
for developer purpose (instead of getting raw dict without any hint about what is in it).
"""

from novu.dto.change import ChangeDetailDto, ChangeDto, PaginatedChangeDto
from novu.dto.event import EventDto
from novu.dto.field import FieldFilterPartDto
from novu.dto.integration import IntegrationChannelUsageDto, IntegrationDto
from novu.dto.layout import LayoutDto, LayoutVariableDto, PaginatedLayoutDto
from novu.dto.notification_group import (
    NotificationGroupDto,
    PaginatedNotificationGroupDto,
)
from novu.dto.notification_template import (
    NotificationStepDto,
    NotificationStepMetadataDto,
    NotificationTemplateDto,
    NotificationTemplateFormDto,
    NotificationTriggerDto,
    NotificationTriggerVariableDto,
    PaginatedNotificationTemplateDto,
)
from novu.dto.step_filter import StepFilterDto
from novu.dto.subscriber import (
    PaginatedSubscriberDto,
    SubscriberDto,
    SubscriberPreferenceChannelDto,
    SubscriberPreferenceDto,
    SubscriberPreferencePreferenceDto,
    SubscriberPreferenceTemplateDto,
)
from novu.dto.topic import PaginatedTopicDto, TopicDto, TriggerTopicDto

__all__ = [
    "ChangeDetailDto",
    "ChangeDto",
    "EventDto",
    "FieldFilterPartDto",
    "IntegrationChannelUsageDto",
    "IntegrationDto",
    "LayoutDto",
    "LayoutVariableDto",
    "NotificationGroupDto",
    "NotificationStepDto",
    "NotificationStepMetadataDto",
    "NotificationTemplateDto",
    "NotificationTemplateFormDto",
    "NotificationTriggerDto",
    "NotificationTriggerVariableDto",
    "PaginatedChangeDto",
    "PaginatedLayoutDto",
    "PaginatedNotificationGroupDto",
    "PaginatedNotificationTemplateDto",
    "PaginatedSubscriberDto",
    "PaginatedTopicDto",
    "StepFilterDto",
    "SubscriberDto",
    "SubscriberPreferenceChannelDto",
    "SubscriberPreferenceDto",
    "SubscriberPreferencePreferenceDto",
    "SubscriberPreferenceTemplateDto",
    "TopicDto",
    "TriggerTopicDto",
]
