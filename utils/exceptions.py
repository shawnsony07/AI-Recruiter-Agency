class ResumeProcessingError(Exception):
    """Base exception for resume processing errors"""

    pass


class ExtractionError(ResumeProcessingError):
    """Raised when resume extraction fails"""

    pass


class AnalysisError(ResumeProcessingError):
    """Raised when resume analysis fails"""

    pass


class MatchingError(ResumeProcessingError):
    """Raised when job matching fails"""

    pass


class ScreeningError(ResumeProcessingError):
    """Raised when candidate screening fails"""

    pass


class RecommendationError(ResumeProcessingError):
    """Raised when generating recommendations fails"""

    pass