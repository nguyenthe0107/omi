from datetime import datetime
from typing import List, Optional
from enum import Enum

from pydantic import BaseModel

from models.memory import Geolocation
from models.transcript_segment import TranscriptSegment


class ProcessingMemoryStatus(str, Enum):
    Capturing = 'capturing'
    Processing = 'processing'
    Done = 'done'


class ProcessingMemory(BaseModel):
    id: str
    session_id: Optional[str] = None
    session_ids: List[str] = []
    audio_url: Optional[str] = None
    created_at: datetime
    capturing_to: Optional[datetime] = None
    status: Optional[ProcessingMemoryStatus] = None
    timer_start: float
    timer_segment_start: Optional[float] = None
    timer_starts: List[float] = []
    language: Optional[str] = None  # applies only to Friend # TODO: once released migrate db to default 'en'
    transcript_segments: List[TranscriptSegment] = []
    geolocation: Optional[Geolocation] = None
    emotional_feedback: Optional[bool] = False

    memory_id: Optional[str] = None
    message_ids: List[str] = []


class BasicProcessingMemory(BaseModel):
    id: str
    timer_start: float
    created_at: datetime
    capturing_to: Optional[datetime] = None
    status: Optional[ProcessingMemoryStatus] = None
    geolocation: Optional[Geolocation] = None
    emotional_feedback: Optional[bool] = False
    memory_id: Optional[str] = None

class DetailProcessingMemory(BaseModel):
    id: str
    timer_start: float
    created_at: datetime
    capturing_to: Optional[datetime] = None
    status: Optional[ProcessingMemoryStatus] = None
    geolocation: Optional[Geolocation] = None
    emotional_feedback: Optional[bool] = False
    transcript_segments: List[TranscriptSegment] = []
    memory_id: Optional[str] = None


class UpdateProcessingMemory(BaseModel):
    id: Optional[str] = None
    capturing_to: Optional[datetime] = None
    geolocation: Optional[Geolocation] = None
    emotional_feedback: Optional[bool] = False


class UpdateProcessingMemoryResponse(BaseModel):
    result: BasicProcessingMemory

class DetailProcessingMemoryResponse(BaseModel):
    result: DetailProcessingMemory


class DetailProcessingMemoriesResponse(BaseModel):
    result: List[DetailProcessingMemory]


class BasicProcessingMemoryResponse(BaseModel):
    result: BasicProcessingMemory


class BasicProcessingMemoriesResponse(BaseModel):
    result: List[BasicProcessingMemory]
