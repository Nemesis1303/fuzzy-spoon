# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: federated.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='federated.proto',
  package='federated',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x66\x65\x64\x65rated.proto\x12\tfederated\"3\n\x0bModelServer\x12$\n\tgradients\x18\x01 \x03(\x0b\x32\x11.federated.Update\"g\n\x0bTensorShape\x12\'\n\x03\x64im\x18\x02 \x03(\x0b\x32\x1a.federated.TensorShape.Dim\x1a/\n\x03\x44im\x12\x0c\n\x04size\x18\x01 \x01(\x03\x12\x11\n\x04name\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_name\"r\n\x06Update\x12\x13\n\x0btensor_name\x18\x01 \x01(\t\x12\r\n\x05\x64type\x18\x02 \x01(\t\x12,\n\x0ctensor_shape\x18\x03 \x01(\x0b\x32\x16.federated.TensorShape\x12\x16\n\x0etensor_content\x18\x04 \x01(\x0c\"\x89\x01\n\x15MessageAdditionalData\x12\x1c\n\x14\x66\x65\x64\x65ration_completed\x18\x01 \x01(\x08\x12\x1b\n\x13iteration_completed\x18\x02 \x01(\x08\x12\x19\n\x11\x63urrent_iteration\x18\x03 \x01(\r\x12\x1a\n\x12num_max_iterations\x18\x04 \x01(\r\"\xbd\x01\n\rMessageHeader\x12\x17\n\nid_request\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0bid_response\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1a\n\rid_to_request\x18\x03 \x01(\tH\x02\x88\x01\x01\x12,\n\x0cmessage_type\x18\x04 \x01(\x0e\x32\x16.federated.MessageTypeB\r\n\x0b_id_requestB\x0e\n\x0c_id_responseB\x10\n\x0e_id_to_request\"\x94\x01\n\x13\x43lientTensorRequest\x12(\n\x06header\x18\x01 \x01(\x0b\x32\x18.federated.MessageHeader\x12\x32\n\x08metadata\x18\x02 \x01(\x0b\x32 .federated.MessageAdditionalData\x12\x1f\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x11.federated.Update\"\x9e\x01\n\x1dServerAggregatedTensorRequest\x12(\n\x06header\x18\x01 \x01(\x0b\x32\x18.federated.MessageHeader\x12\x32\n\x08metadata\x18\x02 \x01(\x0b\x32 .federated.MessageAdditionalData\x12\x1f\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x11.federated.Update\"v\n\x16\x43lientReceivedResponse\x12(\n\x06header\x18\x01 \x01(\x0b\x32\x18.federated.MessageHeader\x12\x32\n\x08metadata\x18\x02 \x01(\x0b\x32 .federated.MessageAdditionalData\"v\n\x16ServerReceivedResponse\x12(\n\x06header\x18\x01 \x01(\x0b\x32\x18.federated.MessageHeader\x12\x32\n\x08metadata\x18\x02 \x01(\x0b\x32 .federated.MessageAdditionalData*\x82\x01\n\x0bMessageType\x12\x16\n\x12\x43LIENT_TENSOR_SEND\x10\x00\x12\x1b\n\x17\x43LIENT_CONFIRM_RECEIVED\x10\x01\x12!\n\x1dSERVER_AGGREGATED_TENSOR_SEND\x10\x02\x12\x1b\n\x17SERVER_CONFIRM_RECEIVED\x10\x03\x32\xcb\x01\n\nFederation\x12V\n\x0fsendLocalTensor\x12\x1e.federated.ClientTensorRequest\x1a!.federated.ServerReceivedResponse\"\x00\x12\x65\n\x14sendAggregatedTensor\x12(.federated.ServerAggregatedTensorRequest\x1a!.federated.ClientReceivedResponse\"\x00\x62\x06proto3'
)

_MESSAGETYPE = _descriptor.EnumDescriptor(
  name='MessageType',
  full_name='federated.MessageType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CLIENT_TENSOR_SEND', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLIENT_CONFIRM_RECEIVED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SERVER_AGGREGATED_TENSOR_SEND', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SERVER_CONFIRM_RECEIVED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1189,
  serialized_end=1319,
)
_sym_db.RegisterEnumDescriptor(_MESSAGETYPE)

MessageType = enum_type_wrapper.EnumTypeWrapper(_MESSAGETYPE)
CLIENT_TENSOR_SEND = 0
CLIENT_CONFIRM_RECEIVED = 1
SERVER_AGGREGATED_TENSOR_SEND = 2
SERVER_CONFIRM_RECEIVED = 3



_MODELSERVER = _descriptor.Descriptor(
  name='ModelServer',
  full_name='federated.ModelServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gradients', full_name='federated.ModelServer.gradients', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=81,
)


_TENSORSHAPE_DIM = _descriptor.Descriptor(
  name='Dim',
  full_name='federated.TensorShape.Dim',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='federated.TensorShape.Dim.size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='federated.TensorShape.Dim.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_name', full_name='federated.TensorShape.Dim._name',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=139,
  serialized_end=186,
)

_TENSORSHAPE = _descriptor.Descriptor(
  name='TensorShape',
  full_name='federated.TensorShape',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dim', full_name='federated.TensorShape.dim', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TENSORSHAPE_DIM, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=186,
)


_UPDATE = _descriptor.Descriptor(
  name='Update',
  full_name='federated.Update',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensor_name', full_name='federated.Update.tensor_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='federated.Update.dtype', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tensor_shape', full_name='federated.Update.tensor_shape', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tensor_content', full_name='federated.Update.tensor_content', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=302,
)


_MESSAGEADDITIONALDATA = _descriptor.Descriptor(
  name='MessageAdditionalData',
  full_name='federated.MessageAdditionalData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='federation_completed', full_name='federated.MessageAdditionalData.federation_completed', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='iteration_completed', full_name='federated.MessageAdditionalData.iteration_completed', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='current_iteration', full_name='federated.MessageAdditionalData.current_iteration', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_max_iterations', full_name='federated.MessageAdditionalData.num_max_iterations', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=305,
  serialized_end=442,
)


_MESSAGEHEADER = _descriptor.Descriptor(
  name='MessageHeader',
  full_name='federated.MessageHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_request', full_name='federated.MessageHeader.id_request', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id_response', full_name='federated.MessageHeader.id_response', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id_to_request', full_name='federated.MessageHeader.id_to_request', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message_type', full_name='federated.MessageHeader.message_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_id_request', full_name='federated.MessageHeader._id_request',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_id_response', full_name='federated.MessageHeader._id_response',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_id_to_request', full_name='federated.MessageHeader._id_to_request',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=445,
  serialized_end=634,
)


_CLIENTTENSORREQUEST = _descriptor.Descriptor(
  name='ClientTensorRequest',
  full_name='federated.ClientTensorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='federated.ClientTensorRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='federated.ClientTensorRequest.metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='federated.ClientTensorRequest.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=637,
  serialized_end=785,
)


_SERVERAGGREGATEDTENSORREQUEST = _descriptor.Descriptor(
  name='ServerAggregatedTensorRequest',
  full_name='federated.ServerAggregatedTensorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='federated.ServerAggregatedTensorRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='federated.ServerAggregatedTensorRequest.metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='federated.ServerAggregatedTensorRequest.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=788,
  serialized_end=946,
)


_CLIENTRECEIVEDRESPONSE = _descriptor.Descriptor(
  name='ClientReceivedResponse',
  full_name='federated.ClientReceivedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='federated.ClientReceivedResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='federated.ClientReceivedResponse.metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=948,
  serialized_end=1066,
)


_SERVERRECEIVEDRESPONSE = _descriptor.Descriptor(
  name='ServerReceivedResponse',
  full_name='federated.ServerReceivedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='federated.ServerReceivedResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='federated.ServerReceivedResponse.metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1068,
  serialized_end=1186,
)

_MODELSERVER.fields_by_name['gradients'].message_type = _UPDATE
_TENSORSHAPE_DIM.containing_type = _TENSORSHAPE
_TENSORSHAPE_DIM.oneofs_by_name['_name'].fields.append(
  _TENSORSHAPE_DIM.fields_by_name['name'])
_TENSORSHAPE_DIM.fields_by_name['name'].containing_oneof = _TENSORSHAPE_DIM.oneofs_by_name['_name']
_TENSORSHAPE.fields_by_name['dim'].message_type = _TENSORSHAPE_DIM
_UPDATE.fields_by_name['tensor_shape'].message_type = _TENSORSHAPE
_MESSAGEHEADER.fields_by_name['message_type'].enum_type = _MESSAGETYPE
_MESSAGEHEADER.oneofs_by_name['_id_request'].fields.append(
  _MESSAGEHEADER.fields_by_name['id_request'])
_MESSAGEHEADER.fields_by_name['id_request'].containing_oneof = _MESSAGEHEADER.oneofs_by_name['_id_request']
_MESSAGEHEADER.oneofs_by_name['_id_response'].fields.append(
  _MESSAGEHEADER.fields_by_name['id_response'])
_MESSAGEHEADER.fields_by_name['id_response'].containing_oneof = _MESSAGEHEADER.oneofs_by_name['_id_response']
_MESSAGEHEADER.oneofs_by_name['_id_to_request'].fields.append(
  _MESSAGEHEADER.fields_by_name['id_to_request'])
_MESSAGEHEADER.fields_by_name['id_to_request'].containing_oneof = _MESSAGEHEADER.oneofs_by_name['_id_to_request']
_CLIENTTENSORREQUEST.fields_by_name['header'].message_type = _MESSAGEHEADER
_CLIENTTENSORREQUEST.fields_by_name['metadata'].message_type = _MESSAGEADDITIONALDATA
_CLIENTTENSORREQUEST.fields_by_name['data'].message_type = _UPDATE
_SERVERAGGREGATEDTENSORREQUEST.fields_by_name['header'].message_type = _MESSAGEHEADER
_SERVERAGGREGATEDTENSORREQUEST.fields_by_name['metadata'].message_type = _MESSAGEADDITIONALDATA
_SERVERAGGREGATEDTENSORREQUEST.fields_by_name['data'].message_type = _UPDATE
_CLIENTRECEIVEDRESPONSE.fields_by_name['header'].message_type = _MESSAGEHEADER
_CLIENTRECEIVEDRESPONSE.fields_by_name['metadata'].message_type = _MESSAGEADDITIONALDATA
_SERVERRECEIVEDRESPONSE.fields_by_name['header'].message_type = _MESSAGEHEADER
_SERVERRECEIVEDRESPONSE.fields_by_name['metadata'].message_type = _MESSAGEADDITIONALDATA
DESCRIPTOR.message_types_by_name['ModelServer'] = _MODELSERVER
DESCRIPTOR.message_types_by_name['TensorShape'] = _TENSORSHAPE
DESCRIPTOR.message_types_by_name['Update'] = _UPDATE
DESCRIPTOR.message_types_by_name['MessageAdditionalData'] = _MESSAGEADDITIONALDATA
DESCRIPTOR.message_types_by_name['MessageHeader'] = _MESSAGEHEADER
DESCRIPTOR.message_types_by_name['ClientTensorRequest'] = _CLIENTTENSORREQUEST
DESCRIPTOR.message_types_by_name['ServerAggregatedTensorRequest'] = _SERVERAGGREGATEDTENSORREQUEST
DESCRIPTOR.message_types_by_name['ClientReceivedResponse'] = _CLIENTRECEIVEDRESPONSE
DESCRIPTOR.message_types_by_name['ServerReceivedResponse'] = _SERVERRECEIVEDRESPONSE
DESCRIPTOR.enum_types_by_name['MessageType'] = _MESSAGETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModelServer = _reflection.GeneratedProtocolMessageType('ModelServer', (_message.Message,), {
  'DESCRIPTOR' : _MODELSERVER,
  '__module__' : 'federated_pb2'
  # @@protoc_insertion_point(class_scope:federated.ModelServer)
  })
_sym_db.RegisterMessage(ModelServer)

TensorShape = _reflection.GeneratedProtocolMessageType('TensorShape', (_message.Message,), {

  'Dim' : _reflection.GeneratedProtocolMessageType('Dim', (_message.Message,), {
    'DESCRIPTOR' : _TENSORSHAPE_DIM,
    '__module__' : 'federated_pb2'
    # @@protoc_insertion_point(class_scope:federated.TensorShape.Dim)
    })
  ,
  'DESCRIPTOR' : _TENSORSHAPE,
  '__module__' : 'federated_pb2'
  # @@protoc_insertion_point(class_scope:federated.TensorShape)
  })
_sym_db.RegisterMessage(TensorShape)
_sym_db.RegisterMessage(TensorShape.Dim)

Update = _reflection.GeneratedProtocolMessageType('Update', (_message.Message,), {
  'DESCRIPTOR' : _UPDATE,
  '__module__' : 'federated_pb2'
  # @@protoc_insertion_point(class_scope:federated.Update)
  })
_sym_db.RegisterMessage(Update)

MessageAdditionalData = _reflection.GeneratedProtocolMessageType('MessageAdditionalData', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEADDITIONALDATA,
  '__module__' : 'federated_pb2'
  # @@protoc_insertion_point(class_scope:federated.MessageAdditionalData)
  })
_sym_db.RegisterMessage(MessageAdditionalData)

MessageHeader = _reflection.GeneratedProtocolMessageType('MessageHeader', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEHEADER,
  '__module__' : 'federated_pb2'
  # @@protoc_insertion_point(class_scope:federated.MessageHeader)
  })
_sym_db.RegisterMessage(MessageHeader)

ClientTensorRequest = _reflection.GeneratedProtocolMessageType('ClientTensorRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTTENSORREQUEST,
  '__module__' : 'federated_pb2'
  # @@protoc_insertion_point(class_scope:federated.ClientTensorRequest)
  })
_sym_db.RegisterMessage(ClientTensorRequest)

ServerAggregatedTensorRequest = _reflection.GeneratedProtocolMessageType('ServerAggregatedTensorRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVERAGGREGATEDTENSORREQUEST,
  '__module__' : 'federated_pb2'
  # @@protoc_insertion_point(class_scope:federated.ServerAggregatedTensorRequest)
  })
_sym_db.RegisterMessage(ServerAggregatedTensorRequest)

ClientReceivedResponse = _reflection.GeneratedProtocolMessageType('ClientReceivedResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTRECEIVEDRESPONSE,
  '__module__' : 'federated_pb2'
  # @@protoc_insertion_point(class_scope:federated.ClientReceivedResponse)
  })
_sym_db.RegisterMessage(ClientReceivedResponse)

ServerReceivedResponse = _reflection.GeneratedProtocolMessageType('ServerReceivedResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVERRECEIVEDRESPONSE,
  '__module__' : 'federated_pb2'
  # @@protoc_insertion_point(class_scope:federated.ServerReceivedResponse)
  })
_sym_db.RegisterMessage(ServerReceivedResponse)



_FEDERATION = _descriptor.ServiceDescriptor(
  name='Federation',
  full_name='federated.Federation',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1322,
  serialized_end=1525,
  methods=[
  _descriptor.MethodDescriptor(
    name='sendLocalTensor',
    full_name='federated.Federation.sendLocalTensor',
    index=0,
    containing_service=None,
    input_type=_CLIENTTENSORREQUEST,
    output_type=_SERVERRECEIVEDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='sendAggregatedTensor',
    full_name='federated.Federation.sendAggregatedTensor',
    index=1,
    containing_service=None,
    input_type=_SERVERAGGREGATEDTENSORREQUEST,
    output_type=_CLIENTRECEIVEDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FEDERATION)

DESCRIPTOR.services_by_name['Federation'] = _FEDERATION

# @@protoc_insertion_point(module_scope)
