# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ratings_features_user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bratings_features_user.proto\x12\x15ratings.features.user\x1a\x1bgoogle/protobuf/empty.proto\"\x1d\n\x0fRegisterRequest\x12\n\n\x02id\x18\x01 \x01(\t\"!\n\x10RegisterResponse\x12\r\n\x05token\x18\x01 \x01(\t\"!\n\x13\x41uthenticateRequest\x12\n\n\x02id\x18\x01 \x01(\t\"%\n\x14\x41uthenticateResponse\x12\r\n\x05token\x18\x01 \x01(\t\"\x1f\n\x10ListVotesRequest\x12\x0b\n\x03\x61pp\x18\x01 \x01(\t\"_\n\x11ListVotesResponse\x12\x0f\n\x07snap_id\x18\x01 \x01(\t\x12\x15\n\rsnap_revision\x18\x02 \x01(\t\x12\x0f\n\x07vote_up\x18\x03 \x01(\x08\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\"F\n\x0bVoteRequest\x12\x0f\n\x07snap_id\x18\x01 \x01(\t\x12\x15\n\rsnap_revision\x18\x02 \x01(\x05\x12\x0f\n\x07vote_up\x18\x03 \x01(\x08\x32\xb4\x03\n\x04User\x12]\n\x08Register\x12&.ratings.features.user.RegisterRequest\x1a\'.ratings.features.user.RegisterResponse\"\x00\x12i\n\x0c\x41uthenticate\x12*.ratings.features.user.AuthenticateRequest\x1a+.ratings.features.user.AuthenticateResponse\"\x00\x12:\n\x06\x44\x65lete\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12\x44\n\x04Vote\x12\".ratings.features.user.VoteRequest\x1a\x16.google.protobuf.Empty\"\x00\x12`\n\tListVotes\x12\'.ratings.features.user.ListVotesRequest\x1a(.ratings.features.user.ListVotesResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ratings_features_user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_REGISTERREQUEST']._serialized_start=83
  _globals['_REGISTERREQUEST']._serialized_end=112
  _globals['_REGISTERRESPONSE']._serialized_start=114
  _globals['_REGISTERRESPONSE']._serialized_end=147
  _globals['_AUTHENTICATEREQUEST']._serialized_start=149
  _globals['_AUTHENTICATEREQUEST']._serialized_end=182
  _globals['_AUTHENTICATERESPONSE']._serialized_start=184
  _globals['_AUTHENTICATERESPONSE']._serialized_end=221
  _globals['_LISTVOTESREQUEST']._serialized_start=223
  _globals['_LISTVOTESREQUEST']._serialized_end=254
  _globals['_LISTVOTESRESPONSE']._serialized_start=256
  _globals['_LISTVOTESRESPONSE']._serialized_end=351
  _globals['_VOTEREQUEST']._serialized_start=353
  _globals['_VOTEREQUEST']._serialized_end=423
  _globals['_USER']._serialized_start=426
  _globals['_USER']._serialized_end=862
# @@protoc_insertion_point(module_scope)
