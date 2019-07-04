// Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

package com.digitalasset.platform

import com.digitalasset.platform.PlatformApplications.RemoteApiEndpoint

/**
  * Specifies configuration for testing remote Ledger API endpoint(s).
  */
sealed abstract class RemoteApiEndpointMode extends Product with Serializable

object RemoteApiEndpointMode {

  /**
    * Single endpoint configuration.
    */
  final case class Single(endpoint: RemoteApiEndpoint) extends RemoteApiEndpointMode

  /**
    * Multi-endpoint configuration driven by a party -> endpoint mapping stored in the provided file.
    */
  final case class MultiFromMapping(mapping: Map[Option[String], RemoteApiEndpoint])
      extends RemoteApiEndpointMode
}