import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from gibson.auth.v1 import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEVERITY_UNSPECIFIED: _ClassVar[Severity]
    SEVERITY_CRITICAL: _ClassVar[Severity]
    SEVERITY_HIGH: _ClassVar[Severity]
    SEVERITY_MEDIUM: _ClassVar[Severity]
    SEVERITY_LOW: _ClassVar[Severity]
    SEVERITY_INFO: _ClassVar[Severity]
    SEVERITY_INFORMATIONAL: _ClassVar[Severity]
SEVERITY_UNSPECIFIED: Severity
SEVERITY_CRITICAL: Severity
SEVERITY_HIGH: Severity
SEVERITY_MEDIUM: Severity
SEVERITY_LOW: Severity
SEVERITY_INFO: Severity
SEVERITY_INFORMATIONAL: Severity

class TimeRange(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: _timestamp_pb2.Timestamp
    end: _timestamp_pb2.Timestamp
    def __init__(self, start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetRecurringVulnerabilitiesRequest(_message.Message):
    __slots__ = ("threshold", "time_range", "severities", "target_types", "limit", "offset")
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    SEVERITIES_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPES_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    threshold: int
    time_range: TimeRange
    severities: _containers.RepeatedScalarFieldContainer[Severity]
    target_types: _containers.RepeatedScalarFieldContainer[str]
    limit: int
    offset: int
    def __init__(self, threshold: _Optional[int] = ..., time_range: _Optional[_Union[TimeRange, _Mapping]] = ..., severities: _Optional[_Iterable[_Union[Severity, str]]] = ..., target_types: _Optional[_Iterable[str]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class GetRecurringVulnerabilitiesResponse(_message.Message):
    __slots__ = ("vulnerabilities", "total_count", "time_range")
    VULNERABILITIES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    vulnerabilities: _containers.RepeatedCompositeFieldContainer[RecurringVulnerability]
    total_count: int
    time_range: TimeRange
    def __init__(self, vulnerabilities: _Optional[_Iterable[_Union[RecurringVulnerability, _Mapping]]] = ..., total_count: _Optional[int] = ..., time_range: _Optional[_Union[TimeRange, _Mapping]] = ...) -> None: ...

class RecurringVulnerability(_message.Message):
    __slots__ = ("vuln_type", "cve_ids", "cwe_ids", "occurrence_count", "affected_host_count", "severity_distribution", "first_seen", "last_seen", "sample_hosts")
    class SeverityDistributionEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    VULN_TYPE_FIELD_NUMBER: _ClassVar[int]
    CVE_IDS_FIELD_NUMBER: _ClassVar[int]
    CWE_IDS_FIELD_NUMBER: _ClassVar[int]
    OCCURRENCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_HOST_COUNT_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    FIRST_SEEN_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_HOSTS_FIELD_NUMBER: _ClassVar[int]
    vuln_type: str
    cve_ids: _containers.RepeatedScalarFieldContainer[str]
    cwe_ids: _containers.RepeatedScalarFieldContainer[str]
    occurrence_count: int
    affected_host_count: int
    severity_distribution: _containers.ScalarMap[str, int]
    first_seen: _timestamp_pb2.Timestamp
    last_seen: _timestamp_pb2.Timestamp
    sample_hosts: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, vuln_type: _Optional[str] = ..., cve_ids: _Optional[_Iterable[str]] = ..., cwe_ids: _Optional[_Iterable[str]] = ..., occurrence_count: _Optional[int] = ..., affected_host_count: _Optional[int] = ..., severity_distribution: _Optional[_Mapping[str, int]] = ..., first_seen: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_seen: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., sample_hosts: _Optional[_Iterable[str]] = ...) -> None: ...

class GetRemediationMetricsRequest(_message.Message):
    __slots__ = ("vuln_type", "time_range", "group_by")
    VULN_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    vuln_type: str
    time_range: TimeRange
    group_by: str
    def __init__(self, vuln_type: _Optional[str] = ..., time_range: _Optional[_Union[TimeRange, _Mapping]] = ..., group_by: _Optional[str] = ...) -> None: ...

class GetRemediationMetricsResponse(_message.Message):
    __slots__ = ("metrics", "overall_rate", "overall_mttr", "time_range", "data_limitations")
    METRICS_FIELD_NUMBER: _ClassVar[int]
    OVERALL_RATE_FIELD_NUMBER: _ClassVar[int]
    OVERALL_MTTR_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    DATA_LIMITATIONS_FIELD_NUMBER: _ClassVar[int]
    metrics: _containers.RepeatedCompositeFieldContainer[RemediationMetric]
    overall_rate: float
    overall_mttr: float
    time_range: TimeRange
    data_limitations: str
    def __init__(self, metrics: _Optional[_Iterable[_Union[RemediationMetric, _Mapping]]] = ..., overall_rate: _Optional[float] = ..., overall_mttr: _Optional[float] = ..., time_range: _Optional[_Union[TimeRange, _Mapping]] = ..., data_limitations: _Optional[str] = ...) -> None: ...

class RemediationMetric(_message.Message):
    __slots__ = ("group_key", "group_value", "remediation_rate", "mttr", "recurrence_rate", "total_findings", "remediated_findings", "trend_vs_previous")
    GROUP_KEY_FIELD_NUMBER: _ClassVar[int]
    GROUP_VALUE_FIELD_NUMBER: _ClassVar[int]
    REMEDIATION_RATE_FIELD_NUMBER: _ClassVar[int]
    MTTR_FIELD_NUMBER: _ClassVar[int]
    RECURRENCE_RATE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FINDINGS_FIELD_NUMBER: _ClassVar[int]
    REMEDIATED_FINDINGS_FIELD_NUMBER: _ClassVar[int]
    TREND_VS_PREVIOUS_FIELD_NUMBER: _ClassVar[int]
    group_key: str
    group_value: str
    remediation_rate: float
    mttr: float
    recurrence_rate: float
    total_findings: int
    remediated_findings: int
    trend_vs_previous: float
    def __init__(self, group_key: _Optional[str] = ..., group_value: _Optional[str] = ..., remediation_rate: _Optional[float] = ..., mttr: _Optional[float] = ..., recurrence_rate: _Optional[float] = ..., total_findings: _Optional[int] = ..., remediated_findings: _Optional[int] = ..., trend_vs_previous: _Optional[float] = ...) -> None: ...

class GetAssetRiskScoreRequest(_message.Message):
    __slots__ = ("asset_id", "algorithm", "include_history", "limit")
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_HISTORY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    asset_id: str
    algorithm: str
    include_history: bool
    limit: int
    def __init__(self, asset_id: _Optional[str] = ..., algorithm: _Optional[str] = ..., include_history: bool = ..., limit: _Optional[int] = ...) -> None: ...

class GetAssetRiskScoreResponse(_message.Message):
    __slots__ = ("assets", "portfolio_risk_score", "portfolio_risk_tier")
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    PORTFOLIO_RISK_SCORE_FIELD_NUMBER: _ClassVar[int]
    PORTFOLIO_RISK_TIER_FIELD_NUMBER: _ClassVar[int]
    assets: _containers.RepeatedCompositeFieldContainer[AssetRiskScore]
    portfolio_risk_score: float
    portfolio_risk_tier: str
    def __init__(self, assets: _Optional[_Iterable[_Union[AssetRiskScore, _Mapping]]] = ..., portfolio_risk_score: _Optional[float] = ..., portfolio_risk_tier: _Optional[str] = ...) -> None: ...

class AssetRiskScore(_message.Message):
    __slots__ = ("asset_id", "asset_name", "score", "tier", "factors", "trend_vs_previous", "recommendations", "historical_scores")
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_NAME_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    FACTORS_FIELD_NUMBER: _ClassVar[int]
    TREND_VS_PREVIOUS_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDATIONS_FIELD_NUMBER: _ClassVar[int]
    HISTORICAL_SCORES_FIELD_NUMBER: _ClassVar[int]
    asset_id: str
    asset_name: str
    score: float
    tier: str
    factors: _containers.RepeatedCompositeFieldContainer[RiskFactor]
    trend_vs_previous: float
    recommendations: _containers.RepeatedScalarFieldContainer[str]
    historical_scores: _containers.RepeatedCompositeFieldContainer[HistoricalRiskScore]
    def __init__(self, asset_id: _Optional[str] = ..., asset_name: _Optional[str] = ..., score: _Optional[float] = ..., tier: _Optional[str] = ..., factors: _Optional[_Iterable[_Union[RiskFactor, _Mapping]]] = ..., trend_vs_previous: _Optional[float] = ..., recommendations: _Optional[_Iterable[str]] = ..., historical_scores: _Optional[_Iterable[_Union[HistoricalRiskScore, _Mapping]]] = ...) -> None: ...

class RiskFactor(_message.Message):
    __slots__ = ("name", "weight", "value", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    weight: float
    value: float
    description: str
    def __init__(self, name: _Optional[str] = ..., weight: _Optional[float] = ..., value: _Optional[float] = ..., description: _Optional[str] = ...) -> None: ...

class HistoricalRiskScore(_message.Message):
    __slots__ = ("date", "score", "tier")
    DATE_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    date: _timestamp_pb2.Timestamp
    score: float
    tier: str
    def __init__(self, date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., score: _Optional[float] = ..., tier: _Optional[str] = ...) -> None: ...

class GetAttackPatternsRequest(_message.Message):
    __slots__ = ("technique", "target_type", "min_success_rate", "limit")
    TECHNIQUE_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    MIN_SUCCESS_RATE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    technique: str
    target_type: str
    min_success_rate: float
    limit: int
    def __init__(self, technique: _Optional[str] = ..., target_type: _Optional[str] = ..., min_success_rate: _Optional[float] = ..., limit: _Optional[int] = ...) -> None: ...

class GetAttackPatternsResponse(_message.Message):
    __slots__ = ("patterns", "total_patterns")
    PATTERNS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    patterns: _containers.RepeatedCompositeFieldContainer[AttackPattern]
    total_patterns: int
    def __init__(self, patterns: _Optional[_Iterable[_Union[AttackPattern, _Mapping]]] = ..., total_patterns: _Optional[int] = ...) -> None: ...

class AttackPattern(_message.Message):
    __slots__ = ("pattern_id", "technique_chain", "success_rate", "occurrence_count", "target_characteristics", "sample_missions", "confidence")
    class TargetCharacteristicsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PATTERN_ID_FIELD_NUMBER: _ClassVar[int]
    TECHNIQUE_CHAIN_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_RATE_FIELD_NUMBER: _ClassVar[int]
    OCCURRENCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TARGET_CHARACTERISTICS_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_MISSIONS_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    pattern_id: str
    technique_chain: _containers.RepeatedCompositeFieldContainer[TechniqueInChain]
    success_rate: float
    occurrence_count: int
    target_characteristics: _containers.ScalarMap[str, str]
    sample_missions: _containers.RepeatedScalarFieldContainer[str]
    confidence: float
    def __init__(self, pattern_id: _Optional[str] = ..., technique_chain: _Optional[_Iterable[_Union[TechniqueInChain, _Mapping]]] = ..., success_rate: _Optional[float] = ..., occurrence_count: _Optional[int] = ..., target_characteristics: _Optional[_Mapping[str, str]] = ..., sample_missions: _Optional[_Iterable[str]] = ..., confidence: _Optional[float] = ...) -> None: ...

class TechniqueInChain(_message.Message):
    __slots__ = ("technique", "mitre_id", "mitre_name", "position")
    TECHNIQUE_FIELD_NUMBER: _ClassVar[int]
    MITRE_ID_FIELD_NUMBER: _ClassVar[int]
    MITRE_NAME_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    technique: str
    mitre_id: str
    mitre_name: str
    position: int
    def __init__(self, technique: _Optional[str] = ..., mitre_id: _Optional[str] = ..., mitre_name: _Optional[str] = ..., position: _Optional[int] = ...) -> None: ...

class GetSimilarTargetsRequest(_message.Message):
    __slots__ = ("target_id", "k", "features")
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    K_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    target_id: str
    k: int
    features: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, target_id: _Optional[str] = ..., k: _Optional[int] = ..., features: _Optional[_Iterable[str]] = ...) -> None: ...

class GetSimilarTargetsResponse(_message.Message):
    __slots__ = ("reference_target_id", "similar_targets", "features_used")
    REFERENCE_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    SIMILAR_TARGETS_FIELD_NUMBER: _ClassVar[int]
    FEATURES_USED_FIELD_NUMBER: _ClassVar[int]
    reference_target_id: str
    similar_targets: _containers.RepeatedCompositeFieldContainer[SimilarTarget]
    features_used: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, reference_target_id: _Optional[str] = ..., similar_targets: _Optional[_Iterable[_Union[SimilarTarget, _Mapping]]] = ..., features_used: _Optional[_Iterable[str]] = ...) -> None: ...

class SimilarTarget(_message.Message):
    __slots__ = ("target_id", "target_name", "similarity_score", "matching_features", "successful_findings", "recommended_techniques")
    class MatchingFeaturesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: FeatureMatch
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[FeatureMatch, _Mapping]] = ...) -> None: ...
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    SIMILARITY_SCORE_FIELD_NUMBER: _ClassVar[int]
    MATCHING_FEATURES_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFUL_FINDINGS_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_TECHNIQUES_FIELD_NUMBER: _ClassVar[int]
    target_id: str
    target_name: str
    similarity_score: float
    matching_features: _containers.MessageMap[str, FeatureMatch]
    successful_findings: _containers.RepeatedScalarFieldContainer[str]
    recommended_techniques: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, target_id: _Optional[str] = ..., target_name: _Optional[str] = ..., similarity_score: _Optional[float] = ..., matching_features: _Optional[_Mapping[str, FeatureMatch]] = ..., successful_findings: _Optional[_Iterable[str]] = ..., recommended_techniques: _Optional[_Iterable[str]] = ...) -> None: ...

class FeatureMatch(_message.Message):
    __slots__ = ("feature", "overlap", "matched_values")
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    OVERLAP_FIELD_NUMBER: _ClassVar[int]
    MATCHED_VALUES_FIELD_NUMBER: _ClassVar[int]
    feature: str
    overlap: float
    matched_values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, feature: _Optional[str] = ..., overlap: _Optional[float] = ..., matched_values: _Optional[_Iterable[str]] = ...) -> None: ...
