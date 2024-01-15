import injector

from dataclasses import dataclass

@dataclass
class Config:
    interface: type
    cls: type
    scope: type[injector.Scope] | injector.ScopeDecorator | None = None