# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2



_VARIABLE = descriptor.Descriptor(
  name='Variable',
  full_name='variables.Variable',
  filename='variables.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='key', full_name='variables.Variable.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='variables.Variable.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_VARIABLEVECTOR = descriptor.Descriptor(
  name='VariableVector',
  full_name='variables.VariableVector',
  filename='variables.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='variables', full_name='variables.VariableVector.variables', index=0,
      number=1, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_BLINK = descriptor.Descriptor(
  name='Blink',
  full_name='variables.Blink',
  filename='variables.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='index', full_name='variables.Blink.index', index=0,
      number=1, type=5, cpp_type=1, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timestamp', full_name='variables.Blink.timestamp', index=1,
      number=2, type=1, cpp_type=5, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_BLINKVECTOR = descriptor.Descriptor(
  name='BlinkVector',
  full_name='variables.BlinkVector',
  filename='variables.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='blinks', full_name='variables.BlinkVector.blinks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_SAMPLE = descriptor.Descriptor(
  name='Sample',
  full_name='variables.Sample',
  filename='variables.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='value', full_name='variables.Sample.value', index=0,
      number=1, type=1, cpp_type=5, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timestamp', full_name='variables.Sample.timestamp', index=1,
      number=2, type=1, cpp_type=5, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_SAMPLEVECTOR = descriptor.Descriptor(
  name='SampleVector',
  full_name='variables.SampleVector',
  filename='variables.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='samples', full_name='variables.SampleVector.samples', index=0,
      number=1, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_DECISION = descriptor.Descriptor(
  name='Decision',
  full_name='variables.Decision',
  filename='variables.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='decision', full_name='variables.Decision.decision', index=0,
      number=1, type=5, cpp_type=1, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='variables.Decision.type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_UGMUPDATE = descriptor.Descriptor(
  name='UgmUpdate',
  full_name='variables.UgmUpdate',
  filename='variables.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='variables.UgmUpdate.type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='variables.UgmUpdate.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_TAG = descriptor.Descriptor(
  name='Tag',
  full_name='variables.Tag',
  filename='variables.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='start_timestamp', full_name='variables.Tag.start_timestamp', index=0,
      number=1, type=1, cpp_type=5, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='end_timestamp', full_name='variables.Tag.end_timestamp', index=1,
      number=2, type=1, cpp_type=5, label=2,
      default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='variables.Tag.name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='channels', full_name='variables.Tag.channels', index=3,
      number=4, type=9, cpp_type=9, label=2,
      default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='desc', full_name='variables.Tag.desc', index=4,
      number=5, type=11, cpp_type=10, label=1,
      default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_TAGVECTOR = descriptor.Descriptor(
  name='TagVector',
  full_name='variables.TagVector',
  filename='variables.proto',
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='tags', full_name='variables.TagVector.tags', index=0,
      number=1, type=11, cpp_type=10, label=3,
      default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],  # TODO(robinson): Implement.
  enum_types=[
  ],
  options=None)


_VARIABLEVECTOR.fields_by_name['variables'].message_type = _VARIABLE
_BLINKVECTOR.fields_by_name['blinks'].message_type = _BLINK
_SAMPLEVECTOR.fields_by_name['samples'].message_type = _SAMPLE
_TAG.fields_by_name['desc'].message_type = _VARIABLEVECTOR
_TAGVECTOR.fields_by_name['tags'].message_type = _TAG

class Variable(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _VARIABLE

class VariableVector(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _VARIABLEVECTOR

class Blink(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BLINK

class BlinkVector(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BLINKVECTOR

class Sample(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SAMPLE

class SampleVector(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SAMPLEVECTOR

class Decision(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DECISION

class UgmUpdate(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UGMUPDATE

class Tag(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TAG

class TagVector(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TAGVECTOR

