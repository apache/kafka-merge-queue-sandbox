/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements. See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License. You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.apache.kafka.server.storage.log;

public class UnexpectedAppendOffsetException extends RuntimeException {

    public final long firstOffset;
    public final long lastOffset;

    /**
     * Indicates the follower or the future replica received records from the leader (or current
     * replica) with first offset less than expected next offset.
     * @param firstOffset The first offset of the records to append
     * @param lastOffset  The last offset of the records to append
     */
    public UnexpectedAppendOffsetException(String message, long firstOffset, long lastOffset) {
        super(message);
        this.firstOffset = firstOffset;
        this.lastOffset = lastOffset;
    }
}
